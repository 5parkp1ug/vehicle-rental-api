from django.contrib import admin

from inventory.models import Branch, City, VehicleType, VehiclePricing, Vehicle, Inventory


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(VehiclePricing)
class VehiclePricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_type', 'branch', 'price')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'variant')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'branch', 'registration_number')


