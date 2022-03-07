from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class City(models.Model):
    """
    model to store city information
    """
    name = models.CharField('City', max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    """
    model to store Branch information
    """
    name = models.CharField('Branch Name', max_length=100)
    address = models.TextField('Address')
    pin_code = models.PositiveIntegerField(validators=[MinValueValidator(111111), MaxValueValidator(999999)])
    city = models.ForeignKey(City, related_name='branches', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    """
    model to store vehicle type
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class VehiclePricing(models.Model):
    """
    Model to store price of vehicle type per branch
    """
    price = models.DecimalField('Price', max_digits=7, decimal_places=2, help_text='price per hour')

    vehicle_type = models.ForeignKey(VehicleType, related_name='branch_wise_price', on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, related_name='vehicle_price_list', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('branch', 'vehicle_type')

    def __str__(self):
        return f'{self.pk}'


class Vehicle(models.Model):
    """
    model to store different vehicles
    """
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    variant = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField()

    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicles', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.make} {self.model} {self.variant}'


class Inventory(models.Model):
    """
    Model to store
    """
    vehicle = models.ForeignKey(Vehicle, related_name='inventory_list', on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, related_name='available_vehicles', on_delete=models.PROTECT)

    registration_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.registration_number
