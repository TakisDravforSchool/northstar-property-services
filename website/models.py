from django.db import models

# Create your models here.
from django.db import models

class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('Snow Removal', 'Snow Removal'),
        ('Lawn Aeration', 'Lawn Aeration'),
        ('Both', 'Both'),
    ]

    PROPERTY_CHOICES = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    service_needed = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    property_type = models.CharField(max_length=50, choices=PROPERTY_CHOICES)
    additional_details = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service_needed}"