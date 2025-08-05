"""Data Models for how.apps.courses"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from how.apps.mixins import DateTimeMixin

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
    description = RichTextField(help_text=_("Course description"))
    prerequisites = RichTextField(
        null=True,
        blank=True,
        help_text=_("Course prerequisites"),
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text=_("Course duration"),
    )
    students = models.ManyToManyField(
        User,
        related_name="courses",
        through="enrollments.Enrollment",
        help_text=_("Course enrollments"),
    )
    skills = ClusterTaggableManager(
        blank=True,
        through="tags.CourseTag",
        help_text=_("Skills will be gained after completing the course"),
    )

    # Dashboard UI config
    show_in_menus = True
    context_object_name = "course"
    template = "ui/courses/id.html"
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("headline"),
        FieldPanel("description"),
        FieldPanel("prerequisites"),
        FieldPanel("duration"),
        FieldPanel("skills"),
    ]
    page_description = _("Courses")

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("rating"),
        index.FilterField("skills"),
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
        APIField("skills"),
    ]

    parent_page_types = ["categories.Category", "paths.LearningPath"]
    subpage_types = ["modules.Module", "posts.Post"]

    @property
    def student_count(self) -> int:
        """Number of students enrolled in a course"""

        return self.students.count()

    @property
    def get_modules(self):
        """Get modules of a course"""

        return self.get_children().filter(content_type__model="module")

    @property
    def get_module_count(self) -> int:
        """Number of modules of a course"""

        return self.get_children().filter(content_type__model="module").count()
