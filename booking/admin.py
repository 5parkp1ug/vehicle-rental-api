from django.contrib import admin

from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_id', 'status', 'start_time', 'end_time', 'total_cost', 'vehicle', 'user')
