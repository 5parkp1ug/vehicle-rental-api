from django.shortcuts import render
from rest_framework import viewsets, status, views
from rest_framework import mixins
from rest_framework.response import Response

from inventory.models import VehiclePricing, Inventory
from inventory.serializer import BranchSerializer, VehiclePricingSerializer, InventorySerializer


class BranchViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Endpoints to manage branch
    """
    serializer_class = BranchSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehiclePricingViewSet(viewsets.ModelViewSet):

    serializer_class = VehiclePricingSerializer
    queryset = VehiclePricing.objects.all()


class InventoryViewSet(viewsets.ModelViewSet):

    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
