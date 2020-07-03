from address.models import AddressField
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, SET_NULL
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    address = AddressField(on_delete=SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
