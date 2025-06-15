# listings/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
    """
    Represents a single listing in the application.
    """
    id = models.UUIDField(primary_key=True, default=models.UUIDField.get_random_uuid, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"
        ordering = ['-created_at']

    def __str__(self):
        return self.title