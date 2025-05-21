"""Data Models for bayt_al_hikmah.tags"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
class Tag(DateTimeMixin, models.Model):
    """Tags"""

    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text=_("Tag name"),
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text=_("Tag description"),
    )

    def __str__(self) -> str:
        return self.name
