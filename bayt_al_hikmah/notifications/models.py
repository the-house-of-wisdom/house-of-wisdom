"""Data Models for bayt_al_hikmah.notifications"""

from django.db import models
from django.contrib.auth import get_user_model

from bayt_al_hikmah.notifications import NOTIFICATION_TYPES


# Create your models here.
User = get_user_model()


class Notification(models.Model):
    """Notifications"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
        help_text="Notified User",
    )
    type = models.PositiveSmallIntegerField(
        default=1,
        choices=NOTIFICATION_TYPES,
        help_text="Notification type",
    )
    content = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Notification content",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

    def __str__(self) -> str:
        return "self.name"
