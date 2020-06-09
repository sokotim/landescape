from django.urls import path
from .views import station_list_view

app_name = "stations"

urlpatterns = [
    path("", station_list_view, name="list")
]
