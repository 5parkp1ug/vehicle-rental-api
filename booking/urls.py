from django.urls import path

from booking.views import BookingAPIView

urlpatterns = [
    path('booking/', BookingAPIView.as_view())
]