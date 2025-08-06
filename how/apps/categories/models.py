"""Data Models for how.apps.categories"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from how.apps.mixins import DateTimeMixin


# Create your models here.
class CategoryIndex(DateTimeMixin, Page):
    """Category index page"""

    description = RichTextField(help_text=_("Page description"))

    context_object_name = "index"
    template = "ui/categories/index.html"
    content_panels = Page.content_panels + [FieldPanel("description")]
    page_description = _("Category index page")

    parent_page_types = ["home.Home"]
    subpage_types = ["categories.Category"]

    class Meta(Page.Meta):
        """Meta data"""

        verbose_name = _("Category index page")


class Category(DateTimeMixin, Page):
    """Categories"""

    description = RichTextField(help_text=_("Category description"))

    show_in_menus = True
    context_object_name = "category"
    template = "ui/categories/id.html"
    content_panels = Page.content_panels + [FieldPanel("description")]
    page_description = _(
        "Categories help organize courses into thematic or subject-related groupings, "
        "making it easier for users to explore and filter available courses."
    )

    search_fields = Page.search_fields + [index.SearchField("description")]

    api_fields = [APIField("description")]

    parent_page_types = ["categories.CategoryIndex"]
    subpage_types = ["courses.Course", "paths.LearningPath"]

    class Meta:
        """Meta data"""

        verbose_name_plural = "categories"
