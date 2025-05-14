"""Views for bayt_al_hikmah.tags"""

from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    """Home page"""

    template_name = "ui/index.html"
