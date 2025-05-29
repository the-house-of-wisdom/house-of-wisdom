"""Data Models for bayt_al_hikmah.questions"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.questions import QUESTION_TYPES


# Create your models here.
class Question(DateTimeMixin, models.Model):
    """Questions"""

    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="questions",
        help_text=_("Question assignment"),
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=QUESTION_TYPES,
        help_text=_("Question type"),
    )
    text = models.CharField(
        max_length=512,
        db_index=True,
        help_text=_("Question text"),
    )
    order = models.SmallIntegerField(
        default=0,
        help_text=_("Item order in the lesson"),
    )

    def __str__(self) -> str:
        return f"{self.text[:20]}..."
