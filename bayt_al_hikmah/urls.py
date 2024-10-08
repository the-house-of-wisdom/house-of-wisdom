""" URLConf for learn """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bayt_al_hikmah.courses.views import CourseViewSet
from bayt_al_hikmah.items.views import ItemViewSet
from bayt_al_hikmah.modules.views import ModuleViewSet
from bayt_al_hikmah.paths.views import PathViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("courses", CourseViewSet, "course")
router.register("items", ItemViewSet, "item")
router.register("modules", ModuleViewSet, "module")
router.register("paths", PathViewSet, "path")


urlpatterns = [
    path("", include(router.urls)),
]
