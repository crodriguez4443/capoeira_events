# events/views.py
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.conf import settings

class HomePageView(TemplateView):
    template_name = 'events/home.html'

    def get_context_data(self, **kwargs): # class based view for home page
        context = super().get_context_data(**kwargs) # Call the superclass's get_context_data method
        context['events'] = Event.objects.all()  # Retrieve all events from the database
        return context

class CreateEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    permission_required = 'events.add_event'  # Ensure the user has the right to create an event
    success_url = reverse_lazy('home')  # Redirect after a successful form submission

    def form_valid(self, form):
        form.instance.organizer = self.request.user  # Set organizer as the current user
        return super().form_valid(form)

def events(request):
    events = Event.objects.all()  # Retrieve all events from the database
    return render(request, 'events/events.html', {'events': events})

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_details.html', {'event': event})

def edit_event(request, event_id):
    """
    Edit an event by updating its fields with the data from the request.
    Args:
        request (HttpRequest): The HTTP request object.
        event_id (int): The ID of the event to be edited.
    Returns:
        HttpResponse: The HTTP response object with the updated event details.
    """
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        # Update the event's fields with the data from the request
        event.name = request.POST['name']
        event.location = request.POST['location']
        event.address = request.POST['address']
        event.city = request.POST['city']
        event.state = request.POST['state']
        event.zip_code = request.POST['zip_code']
        event.description = request.POST['description']
        event.image = request.POST['image']
        event.category = request.POST['category']
        event.organizer_name = request.POST['organizer_name']
        event.organizer_email = request.POST['organizer_email']
        event.organizer_social_handle = request.POST['organizer_social_handle']
        event.organizer_social_handle_2 = request.POST['organizer_social_handle_2']
        event.date = request.POST['date']
        event.lat = request.POST['lat']
        event.long = request.POST['long']
        
        # Save the updated event to the database
        event.save()
        try:
            db.session.commit()
        except Exception as e:
            print("Failed to commit:", e)
            db.session.rollback()

        # Render the event details template with the updated event
        return render(request, 'events/event_details.html', {'event': event})
        
    return render(request, 'events/edit_event.html', {'event': event})



