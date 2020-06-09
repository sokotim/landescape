from django.db import models
from location_field.models.plain import PlainLocationField


class Station(models.Model):
    address = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=["address"], zoom=7)

    def __str__(self):
        return self.address
