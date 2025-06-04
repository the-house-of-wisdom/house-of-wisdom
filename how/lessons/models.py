"""Data Models for how.lessons"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from how.mixins.models import DateTimeMixin, Orderable
from how.ui.cms.blocks import TextContentBlock


# Create your models here.
class Lesson(DateTimeMixin, Orderable, Page):
    """Lessons"""

    description = StreamField(
        TextContentBlock(),
        help_text=_("Lesson description"),
    )

    # Dashboard UI config
    context_object_name = "lesson"
    template = "ui/previews/lesson.html"
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("order"),
    ]
    page_description = _(
        "Lessons form the core instructional content of a module and may include "
        "text-based materials, videos, quizzes, or interactive exercises."
    )

    # Search fields
    search_fields = Page.search_fields + [index.SearchField("description")]

    # API fields
    api_fields = [APIField("description"), APIField("order")]

    parent_page_types = ["modules.Module"]
    subpage_types = ["assignments.Assignment", "items.Item"]

    def __str__(self) -> str:
        return self.title
