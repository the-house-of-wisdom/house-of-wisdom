""" Data Models for bayt_al_hikmah.tags """

from django.db import models


# Create your models here.
class Tag(models.Model):
    """Tags"""

    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Tag name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Tag description",
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
