from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Booking(models.Model):

    user = models.ForeignKey(
        User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="bookings"
    )
    start = models.DateField(_("start"), auto_now=False, auto_now_add=False)
    end = models.DateField(_("end"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return f"{self.user}: {self.start} - {self.end}"
