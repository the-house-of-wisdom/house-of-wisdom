"""ViewSet Groups"""

from wagtail.admin.viewsets.model import ModelViewSetGroup

from bayt_al_hikmah.cms.views.sets import admin_viewsets, instructor_viewsets


# Create your view set groups here.
class AdminViewSetGroup(ModelViewSetGroup):
    """Admin ViewSetGroup"""

    items = admin_viewsets.values()


class InstructorViewSetGroup(ModelViewSetGroup):
    """Instructor ViewSetGroup"""

    items = instructor_viewsets.values()
