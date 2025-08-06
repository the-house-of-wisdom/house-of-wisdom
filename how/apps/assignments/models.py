"""Data Models for how.apps.assignments"""

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from how.apps.assignments import ASSIGNMENT_TYPES
from how.apps.mixins import DateTimeMixin
from how.cms.blocks import TextBlock


# Create your models here.
class Assignment(DateTimeMixin, Page):
    """Assignments"""

    type = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("Assignment type"),
        choices=ASSIGNMENT_TYPES,
    )
    description = RichTextField(help_text=_("Assignment description"))
    content = StreamField(
        TextBlock(),
        help_text=_("Assignment instructions or more info"),
    )
    is_graded = models.BooleanField(
        default=True,
        help_text=_("Designates if assignment is graded or for practice"),
    )
    is_auto_graded = models.BooleanField(
        default=True,
        help_text=_("Designates if assignment is auto graded"),
    )
    question_count = models.PositiveSmallIntegerField(
        default=10,
        help_text=_("Max number of questions to display (Random Question Selection)"),
    )
    min_percentage = models.FloatField(
        default=80.0,
        help_text=_("Minimum percentage to pass assignment"),
        validators=[
            validators.MinValueValidator(
                0.0, _("Min percentage must be greater than 0")
            ),
            validators.MaxValueValidator(
                100.0, _("Min percentage must be less than 100")
            ),
        ],
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text=_("Designates if assignment is timed"),
    )

    context_object_name = "assignment"
    template = "ui/learn/content/assignment.html"
    content_panels = Page.content_panels + [
        # FieldPanel("type"),
        FieldPanel("description"),
        # FieldPanel("question_count"),
        FieldPanel("min_percentage"),
        FieldPanel("content"),
        FieldPanel("is_graded"),
        FieldPanel("is_auto_graded"),
        InlinePanel("questions", heading="Questions", label="Question"),
    ]
    page_description = _(
        "Lesson Assignments serve as assessments for learners and can include written tasks, "
        "quizzes, coding exercises, or practical applications."
    )

    search_fields = Page.search_fields + [
        index.FilterField("type"),
        index.FilterField("is_auto_graded"),
        index.SearchField("description"),
    ]

    api_fields = [
        APIField("type"),
        APIField("description"),
        APIField("question_count"),
        APIField("min_percentage"),
        APIField("content"),
        APIField("is_auto_graded"),
    ]

    parent_page_types = ["lessons.Lesson"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        """Add extra context"""

        context = super().get_context(request, *args, **kwargs)

        return {
            **context,
            "lesson": context["assignment"].get_parent(),
            "module": context["assignment"].get_parent().get_parent(),
        }
