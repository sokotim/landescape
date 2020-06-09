from django.shortcuts import render
from django.views.generic import ListView
from .models import Station

class StationListView(ListView):
    model = Station

station_list_view = StationListView.as_view()
