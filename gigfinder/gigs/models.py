from django.contrib.gis.db import models

# Create your models here.


class Venue(models.Model):
    """
    Model for a venue
    """
    name = models.CharField(max_length=200)
    location = models.PointField()
