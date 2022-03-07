import math

from django.db.models import Q, F
from django.utils import timezone
from rest_framework import serializers

from booking.models import Booking
from inventory.models import VehicleType, Inventory
from inventory.serializer import VehicleTypeSerializer


class BookingCreateSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)
    vehicle_type = serializers.CharField(required=True)

    def validate_vehicle_type(self, value):
        try:
            vt = VehicleType.objects.get(name=value.lowe())
        except VehicleType.DoesNotExist:
            raise serializers.ValidationError('Vehicle Type does not exist')

        self.context.update({
            'vehicle_type': vt
        })

        return value

    def validate(self, attrs):
        request = self.context.get('request', None)

        if not request:
            raise ValueError('Request required as context in the serializer')

        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        if not start_time > timezone.now():
            raise serializers.ValidationError('Start time should be greater than current time')

        if not end_time > attrs.get('start_time'):
            raise serializers.ValidationError('End time should be greater than start time')


    def create(self, validated_data):
        request = self.context.get('request', None)
        start_time = validated_data.get('start_time')
        end_time = validated_data.get('end_time')
        vehicle_type = self.context.get('vt')
        # check all the booked vehicles for the given time range
        booked_vehicles = Booking.objects.filter(status__in=[Booking.STATUS.BOOKED, Booking.STATUS.ONGOING]). \
            filter(Q(start_time__range=[start_time, end_time]) | Q(end_time__range=[start_time, end_time])). \
            select_related('vehicle__vehicle__vehicle_type'). \
            filter(vehicle__vehicle__vehicle_type=vehicle_type). \
            values_list('vehicle__registration_number', flat=True)

        # fetch all the other vehicles which are available
        available_vehicles = Inventory.objects.select_related('vehicle__vehicle_type'). \
            filter(vehicle__vehicle_type=vehicle_type). \
            filter(~Q(registration_number__in=booked_vehicles)). \
            annotate(price=F('vehicle__vehicle_type__branch_wise_price__price')). \
            order_by('price')

        if not available_vehicles.count():
            raise serializers.ValidationError('No vehicles available for the given vehicle type and time slot')

        else:
            # fetch the vehicle with cheapest price
            free_vehicle = available_vehicles.first()
            duration = end_time - start_time
            duration_in_hour = math.ceil(duration.total_seconds()/3600)

            booking = Booking(
                status=Booking.STATUS.BOOKED,
                start_time=start_time,
                end_time=end_time,
                total_cost=duration_in_hour*free_vehicle.price,
                user=request.user,
                vehicle=free_vehicle
            )
            booking.save()

            return booking


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
