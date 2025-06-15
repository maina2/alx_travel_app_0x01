# listings/serializers.py
from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model, used for read operations.
    """
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price', 'location',
            'category', 'owner_id', 'created_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at']

class ListingCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Listing objects.
    """
    class Meta:
        model = Listing
        fields = [
            'title', 'description', 'price', 'location',
            'category'
        ]
