"""Data Models for how.answers"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable

from how.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Answer(DateTimeMixin, Orderable, models.Model):
    """Question Answers"""

    question = ParentalKey(
        "questions.Question",
        on_delete=models.CASCADE,
        related_name="answers",
        help_text=_("Answer question"),
    )
    is_correct = models.BooleanField(
        default=False,
        help_text=_("Designates if the answer is correct"),
    )
    text = RichTextField(help_text=_("Answer text"))
    feedback = RichTextField(help_text=_("Answer feedback to show after grading"))

    panels = [
        FieldPanel("is_correct"),
        FieldPanel("text"),
        FieldPanel("feedback"),
    ]

    def __str__(self) -> str:
        return f"{self.question}: Answer {self.sort_order}"
