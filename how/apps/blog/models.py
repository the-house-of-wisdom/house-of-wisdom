"""Data Models for how.apps.blog"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from how.apps.mixins import DateTimeMixin
from how.cms.blocks import MediaBlock


# Create your models here.
class Index(DateTimeMixin, Page):
    """Blog index page"""

    context_object_name = "index"
    template = "ui/blog/index.html"
    page_description = _("Blog index page")

    parent_page_types = ["home.Home"]
    subpage_types = ["blog.Article"]

    class Meta(Page.Meta):
        """Meta data"""

        verbose_name = _("Blog index page")

    # TODO: Override `get_context` to sort the articles


class Article(DateTimeMixin, Page):
    """Blog articles"""

    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
        help_text=_("Article image"),
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Article headline"),
    )
    content = StreamField(
        MediaBlock(),
        help_text=_("Article content"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="blog.ArticleTag",
        help_text=_("Article tags"),
    )

    context_object_name = "article"
    template = "ui/blog/article.html"
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("headline"),
        FieldPanel("content"),
        FieldPanel("tags"),
    ]
    page_description = _("News Articles")

    search_fields = Page.search_fields + [
        index.SearchField("headline"),
        index.SearchField("content"),
    ]

    api_fields = [APIField("headline"), APIField("content"), APIField("tags")]

    parent_page_types = ["blog.Index"]
    subpage_types = []

    class Meta(Page.Meta):
        """Meta data"""

        verbose_name = _("News article")


class ArticleTag(TaggedItemBase):
    """Through model for defining m2m rel between Articles and Tags"""

    content_object = ParentalKey(
        Article,
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )
