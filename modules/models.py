""" Data Models for learn.modules """

from django.db import models


# Create your models here.
class Module(models.Model):
    """Modules"""

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        help_text="Module course",
    )
    title = models.CharField(
        max_length=64,
        help_text="Module title",
    )
    description = models.CharField(
        max_length=256,
        help_text="Module description",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    def __str__(self) -> str:
        return f"{self.course}, Module {self.title}"
