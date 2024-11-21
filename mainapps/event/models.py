from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from django.urls import reverse

from mainapps.common.models import GenericModel
User=settings.AUTH_USER_MODEL



class LocationType(models.Model):
    """
    Model representing the type of a location.

    Fields:
    - name: CharField representing the name of the location type (e.g., 'virtual', 'physical').
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EventLocation(models.Model):
    """
    Model representing an external location for an event.

    Fields:
    - name: CharField representing the name or description of the external location.
    - url: URLField representing the external URL of the location.
    """
    name = models.CharField(max_length=100,blank=True,null=True)
    url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name


class Event(GenericModel):
    """
    Model representing an event.

    Fields:
    - user: ForeignKey to User model representing the user who created the event.
    - organiser: ForeignKey to User model representing the user who organized the event.
    - title: CharField representing the title of the event.
    - description: TextField for a detailed description of the event.
    - location_type: ForeignKey to LocationType model representing the type of the event location.
    - event_location: ForeignKey to EventLocation model representing the external location of the event.
    - start_datetime: DateTimeField representing the start date and time of the event.
    - end_datetime: DateTimeField representing the end date and time of the event.
    - participants: Many-to-Many relationship with User representing participants in the event.
    - participant_in_number: total number of people who attended the event
    Methods:
    - __str__: Returns a string representation of the event.
    - get_absolute_url: Returns the absolute URL of the event.

    Meta:
    - ordering: Specifies the default ordering based on the start date and time of the event.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    event_location = models.ForeignKey(EventLocation, on_delete=models.CASCADE, null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    participant_in_number=models.PositiveIntegerField(default=0,blank=True)
    # forms = models.ForeignKey(CustomForm, on_delete=models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return f"{self.organiser.username} created {self.content_type} event, title: {self.title} ({self.object_id})"

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-start_datetime']

class EventOrganiser(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name='organiser')
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='event_organised')

class EventInvitee(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='events_attended')

class Participant(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name='participants')
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='event_participated')