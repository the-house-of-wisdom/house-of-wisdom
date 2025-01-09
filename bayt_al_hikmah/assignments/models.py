""" Data Models for bayt_al_hikmah.assignments """

from django.db import models
from django.core import validators


# Create your models here.
class Assignment(models.Model):
    """Assignments"""

    lesson = models.OneToOneField(
        "lessons.Lesson",
        on_delete=models.CASCADE,
        help_text="Assignment lesson",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Assignment title",
    )
    description = models.TextField(
        help_text="Assignment description",
    )
    min_percentage = models.FloatField(
        default=80.0,
        help_text="Minimum percentage to pass the assignment",
        validators=[
            validators.MinValueValidator(0, "Min percentage must be greater than 0"),
            validators.MaxValueValidator(100, "Min percentage must be less than 100"),
        ],
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text="Assignment content",
    )
    is_manual = models.BooleanField(
        default=False,
        help_text="Weather the assignment graded manually",
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
        return self.title
