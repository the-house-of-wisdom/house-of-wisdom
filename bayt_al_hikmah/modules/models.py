"""Data Models for bayt_al_hikmah.modules"""

from django.db import models

from bayt_al_hikmah.mixins import DateTimeMixin


# Create your models here.
class Module(DateTimeMixin, models.Model):
    """Course Modules"""

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="modules",
        help_text="Module course",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Module title",
    )
    description = models.CharField(
        max_length=256,
        help_text="Module description",
    )

    def __str__(self) -> str:
        return self.title
