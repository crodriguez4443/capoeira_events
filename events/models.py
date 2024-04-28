#events/models.py

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('roda', 'Roda'),
        ('batizado', 'Batizado'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    organizer_name = models.CharField(max_length=255)
    organizer_email = models.EmailField()
    organizer_phone = models.CharField(max_length=15)
    date = models.DateTimeField()

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
