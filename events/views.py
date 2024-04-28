# events/views.py
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

class CreateEventView(PermissionRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    permission_required = 'events.add_event'  # Ensure the user has the right to create an event
    success_url = reverse_lazy('events:event_list')  # Redirect after a successful form submission

    def form_valid(self, form):
        form.instance.organizer = self.request.user  # Set organizer as the current user
        return super().form_valid(form)

class HomePageView(TemplateView):
    template_name = 'events/home.html'