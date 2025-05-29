"""Data Models for bayt_al_hikmah.lessons"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
class Lesson(DateTimeMixin, models.Model):
    """Lessons"""

    module = models.ForeignKey(
        "modules.Module",
        on_delete=models.CASCADE,
        related_name="lessons",
        help_text=_("Lesson module"),
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Lesson name"),
    )
    description = models.CharField(
        max_length=256,
        help_text=_("Lesson description"),
    )
    order = models.SmallIntegerField(
        default=0,
        help_text=_("Module order in the course"),
    )

    def __str__(self) -> str:
        return self.name
