"""Data Models for how.answers"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from how.mixins.models import DateTimeMixin
from how.ui.cms.blocks import TextContentBlock


# Create your models here.
class Answer(DateTimeMixin, Page):
    """Question Answers"""

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

    # Dashboard UI config
    context_object_name = "answer"
    template = "ui/previews/answer.html"
    content_panels = Page.content_panels + [
        FieldPanel("is_correct"),
        FieldPanel("text"),
        FieldPanel("description"),
    ]
    page_description = _("Question Answers")

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("is_correct"),
        index.SearchField("text"),
        index.SearchField("description"),
    ]

    # API fields
    api_fields = [APIField("is_correct"), APIField("text"), APIField("description")]

    parent_page_types = ["questions.Question"]
    subpage_types = []

    def __str__(self) -> str:
        return self.title
