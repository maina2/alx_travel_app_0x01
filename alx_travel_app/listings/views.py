from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer, ListingCreateUpdateSerializer
# Assuming Booking model for completeness
from .serializers import BookingSerializer, BookingCreateUpdateSerializer
from django.contrib.auth.models import User

# Placeholder Booking model; replace with actual import
class Booking:
    pass

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Listing model providing CRUD operations.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_serializer_class(self):
        """
        Use ListingCreateUpdateSerializer for create/update actions.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return ListingCreateUpdateSerializer
        return ListingSerializer

    def perform_create(self, serializer):
        """
        Set the owner to the current user when creating a listing.
        """
        serializer.save(owner=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Booking model providing CRUD operations.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_class(self):
        """
        Use BookingCreateUpdateSerializer for create/update actions.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return BookingCreateUpdateSerializer
        return BookingSerializer

    def perform_create(self, serializer):
        """
        Set the user to the current user when creating a booking.
        """
        serializer.save(user=self.request.user)