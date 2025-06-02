"""Data Models for bayt_al_hikmah.answers"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.ui.cms.blocks import TextContentBlock


# Create your models here.
class Answer(DateTimeMixin, models.Model):
    """Question Answers"""

    question = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
        related_name="answers",
        help_text=_("Answer question"),
    )
    is_correct = models.BooleanField(
        default=False,
        help_text=_("Designates if the answer is correct"),
    )
    text = StreamField(
        TextContentBlock(),
        help_text=_("Answer text"),
    )
    description = StreamField(
        TextContentBlock(),
        help_text=_("Why the answer is correct or wrong"),
    )

    def __str__(self) -> str:
        return f"{self.text[:20]}..."
