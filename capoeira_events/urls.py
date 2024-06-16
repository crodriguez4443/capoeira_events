# capoeira_events/urls.py
from django.contrib import admin
from django.urls import path, include
from events.views import HomePageView, CreateEventView, events, event_details, UpdateEventView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), #homepage
    path('admin/', admin.site.urls),
    path('events/create/', CreateEventView.as_view(), name='create_event'),  # Directly define the event creation URL
    path('events/', events, name='events'),  # Listing events
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('event/<int:pk>/', event_details, name='event_details'),    # Include other URL definitions as needed
    path('event/<int:pk>/edit', UpdateEventView.as_view(), name='edit_event'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
