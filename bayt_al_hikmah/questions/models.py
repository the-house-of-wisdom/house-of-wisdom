"""Data Models for bayt_al_hikmah.questions"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.questions import QUESTION_TYPES
from bayt_al_hikmah.ui.cms.blocks import TextContentBlock


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
    text = StreamField(
        TextContentBlock(),
        help_text=_("Question text"),
    )
    order = models.SmallIntegerField(
        default=0,
        help_text=_("Item order in the lesson"),
    )

    def __str__(self) -> str:
        return f"{self.text[:20]}..."
