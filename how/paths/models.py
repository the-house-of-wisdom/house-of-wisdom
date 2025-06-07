"""Data Models for how.paths"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from how.mixins.models import DateTimeMixin
from how.ui.cms.blocks import PathPrerequisitesBlock


# Create your models here.
User = get_user_model()


class LearningPath(DateTimeMixin, Page):
    """Learning Paths, Paths of related courses"""

    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
        help_text=_("Learning Path image"),
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Learning Path headline"),
    )
    description = RichTextField(help_text=_("Learning Path description"))
    prerequisites = StreamField(
        PathPrerequisitesBlock(),
        null=True,
        blank=True,
        help_text=_("Learning Path prerequisites"),
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text=_("Learning Path duration"),
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        db_index=True,
        help_text=_("Learning Path rating"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="tags.LearningPathTag",
        help_text=_("LearningPath tags"),
    )

    # Dashboard UI config
    show_in_menus = True
    context_object_name = "path"
    template = "ui/previews/path.html"
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("headline"),
        FieldPanel("description"),
        FieldPanel("prerequisites"),
        FieldPanel("duration"),
        FieldPanel("tags"),
    ]
    page_description = _(
        "A learning path is a curated sequence of courses designed to guide learners through a specific subject "
        "area or to help them achieve defined career goals. Learning paths can include prerequisites, recommended courses, "
        "and sequencing information to ensure a cohesive learning experience."
    )

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("rating"),
        index.FilterField("tags"),
        index.SearchField("headline"),
        index.SearchField("description"),
        index.SearchField("prerequisites"),
    ]

    # API fields
    api_fields = [
        APIField("image"),
        APIField("rating"),
        APIField("headline"),
        APIField("description"),
        APIField("prerequisites"),
        APIField("duration"),
        APIField("tags"),
    ]

    parent_page_types = ["categories.Category"]
    subpage_types = ["courses.Course"]

    class Meta:
        """Meta data"""

        verbose_name = "Learning path"

    def __str__(self) -> str:
        return self.title
