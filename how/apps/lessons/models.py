"""Data Models for how.apps.lessons"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from how.apps.mixins import DateTimeMixin


# Create your models here.
class Lesson(DateTimeMixin, Page):
    """Lessons"""

    description = RichTextField(help_text=_("Lesson description"))

    context_object_name = "lesson"
    template = "ui/learn/content/lesson.html"
    content_panels = Page.content_panels + [FieldPanel("description")]
    page_description = _(
        "Lessons form the core instructional content of a module and may include "
        "text-based materials, videos, quizzes, or interactive exercises."
    )

    search_fields = Page.search_fields + [index.SearchField("description")]

    api_fields = [APIField("description")]

    parent_page_types = ["modules.Module"]
    subpage_types = ["assignments.Assignment", "items.Item"]

    def get_context(self, request, *args, **kwargs):
        """Add extra context"""

        context = super().get_context(request, *args, **kwargs)

        return {
            **context,
            "module": context["lesson"].get_parent(),
        }
