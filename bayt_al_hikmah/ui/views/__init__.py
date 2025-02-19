"""UI views"""

from django.views.generic import TemplateView


# Create your template views here.
class IndexView(TemplateView):
    """Home Page"""

    template_name = "ui/public/index.html"


class AboutView(TemplateView):
    """About Page"""

    template_name = "ui/public/about.html"


class ProfileView(TemplateView):
    """Profile Page"""

    template_name = "ui/profile.html"
