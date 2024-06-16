# events/views.py
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse, reverse_lazy
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

def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_details.html', {'event': event})

class UpdateEventView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/edit_event.html'

    def form_valid(self, form):
        form.instance.organizer = self.request.user  # Set organizer as the current user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('event_details', kwargs={'pk': self.object.pk})