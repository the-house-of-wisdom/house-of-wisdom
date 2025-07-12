"""Data Models for how.apps.modules"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.models import Page
from wagtail.search import index

from how.apps.mixins import DateTimeMixin


# Create your models here.
class Module(DateTimeMixin, Page):
    """Course Modules"""

    description = models.CharField(
        max_length=256,
        help_text=_("Module description"),
    )

    # Dashboard UI config
    context_object_name = "module"
    template = "ui/previews/module.html"
    content_panels = Page.content_panels + [FieldPanel("description")]
    page_description = _(
        "Modules represent structured segments of a course and typically "
        "contain lessons, resources, and assessments."
    )

    # Search fields
    search_fields = Page.search_fields + [
        index.SearchField("description"),
    ]

    # API fields
    api_fields = [APIField("description")]

    parent_page_types = ["courses.Course"]
    subpage_types = ["lessons.Lesson"]
