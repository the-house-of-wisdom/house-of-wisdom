"""Data Models for bayt_al_hikmah.questions"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from bayt_al_hikmah.mixins.models import DateTimeMixin, Orderable
from bayt_al_hikmah.questions import QUESTION_TYPES
from bayt_al_hikmah.ui.cms.blocks import TextContentBlock


# Create your models here.
class Question(DateTimeMixin, Orderable, Page):
    """Questions"""

    type = models.PositiveSmallIntegerField(
        default=0,
        choices=QUESTION_TYPES,
        help_text=_("Question type"),
    )
    text = StreamField(
        TextContentBlock(),
        help_text=_("Question text"),
    )

    # Dashboard UI config
    context_object_name = "question"
    template = "ui/previews/question.html"
    content_panels = Page.content_panels + [
        FieldPanel("type"),
        FieldPanel("text"),
        FieldPanel("order"),
    ]
    page_description = _(
        "Questions can be structured as multiple-choice, short answer, "
        "coding exercises, or other formats depending on the assignment type."
    )

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("type"),
        index.SearchField("text"),
    ]

    # API fields
    api_fields = [APIField("type"), APIField("text"), APIField("order")]

    parent_page_types = ["assignments.Assignment"]
    subpage_types = ["answers.Answer"]

    def __str__(self) -> str:
        return self.title
