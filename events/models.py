#events/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('roda', 'Roda'),
        ('batizado', 'Batizado'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    image = models.ImageField(upload_to='event_images/', blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    organizer_name = models.CharField(max_length=255, blank=True, null=True)
    organizer_email = models.EmailField( blank=True, null=True)
    organizer_social_handle = models.CharField(max_length=50, null=True, blank=True)
    organizer_social_handle_2 = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('yes', 'Yes'),
        ('maybe', 'Maybe'),
        ('no', 'No'),
    ]
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='no')

    def __str__(self):
        return f'{self.user.username} - {self.event.name} - {self.status}'
