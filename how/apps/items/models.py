"""Data Models for how.apps.items"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from how.apps.items import ITEM_TYPES
from how.apps.mixins import DateTimeMixin
from how.cms.blocks import MediaBlock


# Create your models here.
class Item(DateTimeMixin, Page):
    """Lesson Items"""

    type = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("Item type"),
        choices=ITEM_TYPES,
    )
    content = StreamField(
        MediaBlock(),
        help_text=_("Item content"),
    )

    context_object_name = "item"
    template = "ui/learn/content/item.html"
    content_panels = Page.content_panels + [FieldPanel("type"), FieldPanel("content")]
    page_description = _(
        "Lesson items represent smaller sections of a lesson, such as individual "
        "text passages, videos, quizzes, or interactive activities."
    )

    search_fields = Page.search_fields + [
        index.FilterField("type"),
        index.SearchField("content"),
    ]

    api_fields = [APIField("type"), APIField("content")]

    parent_page_types = ["lessons.Lesson"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        """Add extra context"""

        context = super().get_context(request, *args, **kwargs)

        return {
            **context,
            "lesson": context["item"].get_parent(),
            "module": context["item"].get_parent().get_parent(),
        }
