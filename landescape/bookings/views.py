from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Booking


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

booking_list_view = BookingListView.as_view()
