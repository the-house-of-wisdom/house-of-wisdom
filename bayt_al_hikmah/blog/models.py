"""Data Models for bayt_al_hikmah.blog"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from bayt_al_hikmah.cms.blocks import CommonContentBlock
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
class Blog(DateTimeMixin, Page):
    """Blog posts"""

    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Blog headline"),
    )
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Blog content"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("headline"),
        index.SearchField("content"),
    ]

    class Meta(Page.Meta):
        """Meta data"""

        verbose_name = _("Blog post")

    def __str__(self) -> str:
        return self.title
