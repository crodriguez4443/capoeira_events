# capoeira_events/urls.py
from django.contrib import admin
from django.urls import path, include
from events.views import HomePageView, CreateEventView, events

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), #homepage
    path('admin/', admin.site.urls),
    path('events/create/', CreateEventView.as_view(), name='create_event'),  # Directly define the event creation URL
    path('events/', events, name='events'),  # Listing events
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    # Include other URL definitions as needed
]

