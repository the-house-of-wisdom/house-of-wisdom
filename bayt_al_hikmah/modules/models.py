""" Data Models for bayt_al_hikmah.modules """

from django.db import models


# Create your models here.
class Module(models.Model):
    """Course Modules"""

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        help_text="Course",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Title",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Description",
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
