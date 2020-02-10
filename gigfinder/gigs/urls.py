from django.conf.urls import url
from gigs.views import LookupView

app_name = 'gigs'

urlpatterns = [
    # Lookup
    url(r'', LookupView.as_view(), name='lookup'),
]
