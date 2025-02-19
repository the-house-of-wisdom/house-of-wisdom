"""Data Models for bayt_al_hikmah.lessons"""

from django.db import models


# Create your models here.
class Lesson(models.Model):
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
    description = models.TextField(
        help_text="Lesson description",
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
        return f"{self.module.course}, Module {self.module}, Lesson {self.name}"
