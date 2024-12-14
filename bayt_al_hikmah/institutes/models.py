""" Data Models for bayt_al_hikmah.institutes """

from django.db import models


# Create your models here.
class Institute(models.Model):
    """Course and learning path providers"""

    image = models.ImageField(
        help_text="Image",
        upload_to="images/institutes/",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Headline",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Description",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the Institute is approved",
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
        return self.name
