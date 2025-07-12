"""Home page"""

from wagtail.models import Page


class Home(Page):
    """Home page"""

    # Dashboard UI
    template = "ui/index.html"
    content_panels = Page.content_panels + []
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["categories.Category"]

    def get_context(self, request, *args, **kwargs):
        """Add extra context to template"""

        return {**super().get_context(request, *args, **kwargs)}
