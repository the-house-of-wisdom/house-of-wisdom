"""Data Models for bayt_al_hikmah.modules"""

from django.db import models


# Create your models here.
class Module(models.Model):
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
    description = models.TextField(
        help_text="Module description",
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
        return f"{self.course}, Module {self.title}"
