# events/forms.py
from django import forms
from .models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'address','city', 'state', 'zip_code', 
                'description', 'image', 'category', 'organizer_name',
                'organizer_email', 'organizer_social_handle', 'date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter event name', 'required': 'required'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'location', 'placeholder': 'Enter location name', 'required': 'required'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address', 'placeholder': 'Enter address', 'required': 'required'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'id': 'city', 'placeholder': 'City', 'required': 'required'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'id': 'state', 'placeholder':'state', 'required': 'required'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'zip_code', 'placeholder': 'Enter zip code', 'required': 'required'}),                  
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'date', 'required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter event description', 'required': 'required'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image', 'required': 'required'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'category', 'required': 'required'}),
            'organizer_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'organizer_name', 'placeholder': 'Enter organizer name', 'required': 'required'}),
            'organizer_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'organizer_email', 'placeholder': 'Enter organizer email', 'required': 'required'}),
            'organizer_social_handle': forms.TextInput(attrs={'class': 'form-control', 'id': 'organizer_social_handle', 'placeholder': 'Enter organizer social handle', 'required': 'not required'}),

        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''  # unspecified path sends the form to the same page
        self.helper.add_input(Submit('submit', 'Save Changes'))