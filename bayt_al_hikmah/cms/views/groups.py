"""ViewSet Groups"""

from wagtail.admin.viewsets.model import ModelViewSetGroup

from bayt_al_hikmah.cms.views.sets import viewsets


# Create your view set groups here.
class CourseViewSetGroup(ModelViewSetGroup):
    """Course ViewSetGroup"""

    items = viewsets.values()
