from django.contrib import admin
from django.forms import ModelForm
from .models import Venue, Event
from floppyforms.gis import PointWidget, BaseGMapWidget
# Register your models here.


class CustomPointWidget(PointWidget, BaseGMapWidget):
    class Media:
        js = ('js/openlayers/OpenLayers.js',
              'https://maps.google.com/maps/api/js?v=3&sensor=false',
              'floppyforms/js/MapWidget.js')
        css = {
            'all': ('css/openLayers/style.css',)
        }


class VenueAdminForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location']
        widgets = {
            'location': CustomPointWidget()
        }


class VenueAdmin(admin.ModelAdmin):
    form = VenueAdminForm


admin.site.register(Venue, VenueAdmin)
admin.site.register(Event)
