from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.


class LookupView(View):
    def get(self, request):
        return render(request, 'gigs/lookup.html')
