"""Home page"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from how.apps.blog.models import Article, Index
from how.apps.categories.models import CategoryIndex
from how.apps.courses.models import Course
from how.apps.paths.models import LearningPath
from how.cms.blocks import MediaBlock


class Home(Page):
    """Home page"""

    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Headline"),
    )
    content = StreamField(
        MediaBlock(),
        help_text=_("Page content"),
    )

    # Dashboard UI
    template = "ui/index.html"
    context_object_name = "home"
    content_panels = Page.content_panels + [FieldPanel("content")]
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = [
        "categories.Category",
        "blog.Index",
        "categories.CategoryIndex",
        "home.About",
        "home.Contact",
    ]

    def get_context(self, request, *args, **kwargs):
        """Add extra context to template"""

        context = super().get_context(request, *args, **kwargs)
        home = context[self.context_object_name]

        return {
            **context,
            "blog": home.get_children().live().type(Index).last(),
            "categories": home.get_children().live().type(CategoryIndex).last(),
            "courses": home.get_descendants().live().type(Course).specific()[:5],
            "paths": home.get_descendants().live().type(LearningPath).specific()[:5],
            "articles": home.get_descendants().live().type(Article).specific()[:5],
        }


class About(Page):
    """About page"""

    content = StreamField(
        MediaBlock(),
        help_text=_("Page content"),
    )

    # Dashboard UI
    template = "ui/about.html"
    context_object_name = "about"
    page_description = _("About us page")
    content_panels = Page.content_panels + [FieldPanel("content")]
    parent_page_types = ["home.Home"]
    subpage_types = []


class Contact(Page):
    """Contact page"""

    content = StreamField(
        MediaBlock(),
        help_text=_("Page content"),
    )

    # Dashboard UI
    template = "ui/contact.html"
    context_object_name = "contact"
    page_description = _("Contact us page")
    content_panels = Page.content_panels + [FieldPanel("content")]
    parent_page_types = ["home.Home"]
    subpage_types = []
