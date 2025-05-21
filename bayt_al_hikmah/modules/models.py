"""Data Models for bayt_al_hikmah.modules"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
class Module(DateTimeMixin, models.Model):
    """Course Modules"""

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="modules",
        help_text=_("Module course"),
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Module title"),
    )
    description = models.CharField(
        max_length=256,
        help_text=_("Module description"),
    )

    def __str__(self) -> str:
        return self.title
