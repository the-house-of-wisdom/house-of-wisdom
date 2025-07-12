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
from how.cms.blocks import CommonContentBlock


# Create your models here.
class Item(DateTimeMixin, Page):
    """Lesson Items"""

    type = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("Item type"),
        choices=ITEM_TYPES,
    )
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Item content"),
    )

    # Dashboard UI config
    context_object_name = "item"
    template = "ui/previews/item.html"
    content_panels = Page.content_panels + [FieldPanel("type"), FieldPanel("content")]
    page_description = _(
        "Lesson items represent smaller sections of a lesson, such as individual "
        "text passages, videos, quizzes, or interactive activities."
    )

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("type"),
        index.SearchField("content"),
    ]

    # API fields
    api_fields = [APIField("type"), APIField("content")]

    parent_page_types = ["lessons.Lesson"]
    subpage_types = []
