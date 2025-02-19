"""Data Models for bayt_al_hikmah.questions"""

from django.db import models

from bayt_al_hikmah.questions import QUESTION_TYPES


# Create your models here.
class Question(models.Model):
    """Questions"""

    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="questions",
        help_text="Question assignment",
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=QUESTION_TYPES,
        help_text="Question type",
    )
    text = models.CharField(
        max_length=512,
        db_index=True,
        help_text="Question text",
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
        return f"{self.assignment}: Question {self.pk}"
