"""Data Models for bayt_al_hikmah.assignments"""

from django.db import models
from django.core import validators
from wagtail.fields import StreamField

from bayt_al_hikmah.cms.blocks import TextContentBlock
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
class Assignment(DateTimeMixin, models.Model):
    """Assignments"""

    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.CASCADE,
        related_name="assignments",
        help_text="Assignment lesson",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Assignment title",
    )
    description = models.CharField(
        max_length=256,
        help_text="Assignment description",
    )
    question_count = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Max questions to display when using random questions",
    )
    min_percentage = models.FloatField(
        default=80.0,
        help_text="Minimum percentage to pass the assignment",
        validators=[
            validators.MinValueValidator(0.0, "Min percentage must be greater than 0"),
            validators.MaxValueValidator(100.0, "Min percentage must be less than 100"),
        ],
    )
    content = StreamField(
        TextContentBlock(),
        help_text="Item content",
    )
    is_auto_graded = models.BooleanField(
        default=True,
        help_text="Weather the assignment graded automatically",
    )

    def __str__(self) -> str:
        return self.title
