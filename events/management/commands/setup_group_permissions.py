# events/management/commands/setup_group_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from events.models import Event, Attendance

class Command(BaseCommand):
    help = 'Sets up initial groups and permissions for the Capoeira events app'

    def handle(self, *args, **options):
        # Create groups
        organizer_group, _ = Group.objects.get_or_create(name='Organizers')
        attendee_group, _ = Group.objects.get_or_create(name='Attendees')

        # Create and assign permissions to Organizer group
        event_content_type = ContentType.objects.get_for_model(Event)
        perm_add_event = Permission.objects.get(codename='add_event', content_type=event_content_type)
        perm_change_event = Permission.objects.get(codename='change_event', content_type=event_content_type)
        perm_delete_event = Permission.objects.get(codename='delete_event', content_type=event_content_type)
        organizer_group.permissions.set([perm_add_event, perm_change_event, perm_delete_event])

        # Create and assign permissions to Attendee group
        attendance_content_type = ContentType.objects.get_for_model(Attendance)
        perm_change_attendance = Permission.objects.create(
            codename='change_attendance',
            name='Can change attendance',
            content_type=attendance_content_type
        )
        attendee_group.permissions.add(perm_change_attendance)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))
