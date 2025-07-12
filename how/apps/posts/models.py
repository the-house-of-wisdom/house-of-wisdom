"""Data Models for how.apps.posts"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from how.apps.mixins import DateTimeMixin
from how.apps.posts import POST_TYPES
from how.cms.blocks import CommonContentBlock

# Create your models here.
User = get_user_model()


class Post(DateTimeMixin, Page):
    """Course Posts"""

    type = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("Post type"),
        choices=POST_TYPES,
    )
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Post content"),
    )

    # Dashboard UI config
    context_object_name = "post"
    template = "ui/previews/post.html"
    content_panels = Page.content_panels + [
        FieldPanel("type"),
        FieldPanel("content"),
    ]
    page_description = _(
        "Posts are designed to allow instructors and course administrators to:"
        "- Publish announcements, updates, or important notices."
        "- Share additional course-related information and supplementary content."
        "- Engage students by keeping them informed about course changes, deadlines, or events."
    )

    # Search fields
    search_fields = Page.search_fields + [
        index.FilterField("type"),
        index.SearchField("content"),
    ]

    # API fields
    api_fields = [APIField("type"), APIField("content")]

    parent_page_types = ["courses.Course"]
    subpage_types = []
