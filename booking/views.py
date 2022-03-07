from django.shortcuts import render

from rest_framework import views, status
from rest_framework.response import Response

from booking.serializer import BookingCreateSerializer, BookingDetailSerializer


class BookingAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = BookingCreateSerializer(data=request.data)

        if serializer.is_valid():
            booking = serializer.save()
            booking_serializer = BookingDetailSerializer(booking)
            return Response(booking_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
