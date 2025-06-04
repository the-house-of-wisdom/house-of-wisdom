"""Data Models for how.notifications"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from how.mixins.models import DateTimeMixin
from how.notifications import NOTIFICATION_TYPES


# Create your models here.
User = get_user_model()


class Notification(DateTimeMixin, models.Model):
    """Notifications"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
        help_text=_("Notified User"),
    )
    type = models.PositiveSmallIntegerField(
        default=1,
        choices=NOTIFICATION_TYPES,
        help_text=_("Notification type"),
    )
    content = models.CharField(
        max_length=256,
        db_index=True,
        help_text=_("Notification content"),
    )

    class Meta:
        """Meta data"""

    def __str__(self) -> str:
        return "self.name"
