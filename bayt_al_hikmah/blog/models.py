"""Data Models for bayt_al_hikmah.blog"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.ui.cms.blocks import CommonContentBlock


# Create your models here.
class Article(DateTimeMixin, Page):
    """Blog articles"""

    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Blog headline"),
    )
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Blog content"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="tags.ArticleTag",
        help_text=_("Course tags"),
    )

    # Dashboard UI config
    context_object_name = "article"
    template = "ui/previews/article.html"
    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("content"),
        FieldPanel("tags"),
    ]
    page_description = _("News Articles")

    # Search fields
    search_fields = Page.search_fields + [
        index.SearchField("headline"),
        index.SearchField("content"),
    ]

    # API fields
    api_fields = [APIField("headline"), APIField("content"), APIField("tags")]

    class Meta(Page.Meta):
        """Meta data"""

        verbose_name = _("News article")

    def __str__(self) -> str:
        return self.title
