"""Wagtail Hooks used to customize the view-level behavior of the Wagtail admin and front-end"""

from wagtail import hooks

from bayt_al_hikmah.cms.views.choosers import chooser_viewsets
from bayt_al_hikmah.cms.views.groups import CourseViewSetGroup
from bayt_al_hikmah.cms.views.sets import CollectionViewSet


# Create your hooks here.
@hooks.register("register_admin_viewset")
def register_views():
    return [
        CollectionViewSet("collections"),
        CourseViewSetGroup(),
        *chooser_viewsets.values(),
    ]
