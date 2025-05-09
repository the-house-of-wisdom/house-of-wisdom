"""Data Models for bayt_al_hikmah.lessons"""

from django.db import models

from bayt_al_hikmah.mixins import DateTimeMixin


# Create your models here.
class Lesson(DateTimeMixin, models.Model):
    """Lessons"""

    module = models.ForeignKey(
        "modules.Module",
        on_delete=models.CASCADE,
        related_name="lessons",
        help_text="Lesson module",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Lesson name",
    )
    description = models.CharField(
        max_length=256,
        help_text="Lesson description",
    )

    def __str__(self) -> str:
        return f"{self.module.course}, Module {self.module}, Lesson {self.name}"
