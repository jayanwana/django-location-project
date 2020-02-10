from django.contrib.gis.db import models

# Create your models here.


class Venue(models.Model):
    """
    Model for a venue
    """
    name = models.CharField(max_length=200)
    location = models.PointField()

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Model for an event
    """
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - {self.venue.name}'
