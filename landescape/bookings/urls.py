from django.urls import path

from .views import booking_list_view

app_name = "bookings"

urlpatterns = [path("", booking_list_view, name="booking_list")]
