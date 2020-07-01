from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    date_hierarchy = "start"
    list_display = ("user", "start", "end")

