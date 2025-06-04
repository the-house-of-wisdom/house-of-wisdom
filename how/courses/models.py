"""Data Models for how.courses"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from how.mixins.models import DateTimeMixin
from how.ui.cms.blocks import CoursePrerequisitesBlock, TextContentBlock


# Create your models here.
User = get_user_model()


class Course(DateTimeMixin, Page):
    """Courses"""

    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,
        help_text=_("Course image"),
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Course headline"),
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        db_index=True,
        help_text=_("Course rating"),
    )
    description = StreamField(
        TextContentBlock(),
        help_text=_("Course description"),
    )
    prerequisites = StreamField(
        CoursePrerequisitesBlock(),
        null=True,
        blank=True,
        help_text=_("Course prerequisites"),
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text=_("Course duration"),
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        help_text=_("Course tags"),
    )
    students = models.ManyToManyField(
        User,
        related_name="students",
        through="enrollments.Enrollment",
        help_text=_("Course enrollments"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="tags.CourseTag",
        help_text=_("Course tags"),
    )

    # Dashboard UI config
    show_in_menus = True
    context_object_name = "course"
    template = "ui/previews/course.html"
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("headline"),
        FieldPanel("description"),
        FieldPanel("prerequisites"),
        FieldPanel("duration"),
        FieldPanel("tags"),
    ]
    page_description = _("Courses")

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

    parent_page_types = ["categories.Category", "paths.LearningPath"]
    subpage_types = ["modules.Module", "posts.Post"]

    def __str__(self) -> str:
        return self.title

    @property
    def student_count(self) -> int:
        """Number of students enrolled in a course"""

        return self.students.count()
