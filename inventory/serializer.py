from rest_framework import serializers

from inventory.models import Branch, VehiclePricing, Inventory


class BranchSerializer(serializers.ModelSerializer):
    """
    Serializer to create, update and delete a branch
    """
    class Meta:
        model = Branch
        fields = '__all__'


class VehiclePricingSerializer(serializers.ModelSerializer):
    vehicle_type = serializers.CharField(source='vehicle_type.name')
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = VehiclePricing
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    vehicle = serializers.CharField(source='vehicle.__str__')
    branch = BranchSerializer()

    class Meta:
        model = Inventory
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
