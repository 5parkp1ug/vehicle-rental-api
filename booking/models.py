from django.db import models

from accounts.models import User
from booking.utils import generate_booking_id
from inventory.models import Inventory


class Booking(models.Model):
    """
    Model to store the bookings
    """
    class STATUS(models.TextChoices):
        BOOKED = 'B', 'Booked'
        ONGOING = 'O', 'Ongoing'
        CANCELLED = 'C', 'Cancelled'
        COMPLETED = 'BC', 'Completed'

    status = models.CharField(choices=STATUS.choices, default=STATUS.BOOKED, max_length=2)
    booking_id = models.CharField(default=generate_booking_id, max_length=8)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Inventory, related_name='bookings', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.booking_id

