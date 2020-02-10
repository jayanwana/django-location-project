from django.shortcuts import render
from django.utils import timezone
from django.views.generic.edit import FormView
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .forms import LookupForm
from .models import Event
# Create your views here.


class LookupView(FormView):

    form_class = LookupForm

    def get(self, request, *args, **kwargs):
        return render(request, 'gigs/lookup.html')

    def form_valid(self, form):
        # Get Data
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']

        # get today's & next week's date
        now = timezone.now()
        next_week = now + timezone.timedelta(weeks=1)

        # get location
        location = Point(longitude, latitude, srid=4326)

        # Lookup Events
        events = Event.objects.filter(datetime__gte=now)\
            .filter(datetime__lte=next_week)\
            .annotate(distance=Distance('venue__location', location))\
            .order_by('distance')[0:5]

        # Render the template
        return render(self.request, 'gigs/lookup_results.html',
                      context={
                          'events': events
                      })
