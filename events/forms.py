# events/forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'address','city', 'state', 'zip_code', 
                'description', 'image', 'category', 'organizer_name',
                'organizer_email', 'organizer_social_handle', 'date']
