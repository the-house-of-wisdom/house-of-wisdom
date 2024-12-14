""" Data Models for bayt_al_hikmah.instructors """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Instructor(models.Model):
    """Instructors"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    institute = models.ForeignKey(
        "institutes.Institute",
        on_delete=models.CASCADE,
        help_text="Institute",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the path is approved",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return self.user
