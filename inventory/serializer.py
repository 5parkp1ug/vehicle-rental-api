from rest_framework import serializers

from inventory.models import Branch, VehiclePricing


class BranchSerializer(serializers.ModelSerializer):
    """
    Serializer to create, update and delete a branch
    """
    class Meta:
        model = Branch
        fields = '__all__'


class VehiclePricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePricing
        fields = '__all__'
