"""Home page"""

from wagtail.models import Page

from how.apps.blog.models import Article, Index
from how.apps.categories.models import Category
from how.apps.courses.models import Course
from how.apps.paths.models import LearningPath


class Home(Page):
    """Home page"""

    # Dashboard UI
    template = "ui/index.html"
    context_object_name = "home"
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["categories.Category", "blog.Index"]

    def get_context(self, request, *args, **kwargs):
        """Add extra context to template"""

        context = super().get_context(request, *args, **kwargs)
        home = context[self.context_object_name]

        return {
            **context,
            "blog": home.get_children().live().type(Index).first(),
            "categories": home.get_children().live().type(Category),
            "courses": home.get_descendants().live().type(Course).specific()[:5],
            "paths": home.get_descendants().live().type(LearningPath).specific()[:5],
            "articles": home.get_descendants().live().type(Article).specific()[:5],
        }
