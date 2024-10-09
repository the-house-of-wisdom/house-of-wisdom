""" URLConf for bayt_al_hikmah """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bayt_al_hikmah.courses.views import CourseViewSet, PathCoursesViewSet
from bayt_al_hikmah.items.views import ItemViewSet, ModuleItemsViewSet
from bayt_al_hikmah.modules.views import CourseModuleViewSet, ModuleViewSet
from bayt_al_hikmah.paths.views import PathViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("courses", CourseViewSet, "course")
router.register("items", ItemViewSet, "item")
router.register("modules", ModuleViewSet, "module")
router.register("paths", PathViewSet, "path")

# Sub-routers
path_router = DefaultRouter()
path_router.register("courses", PathCoursesViewSet, "course")

course_router = DefaultRouter()
course_router.register("modules", CourseModuleViewSet, "module")

module_router = DefaultRouter()
module_router.register("items", ModuleItemsViewSet, "item")


urlpatterns = [
    # Router
    path("", include(router.urls)),
    # Course router
    path(
        "courses/<int:id>/",
        include((course_router.urls, "modules"), namespace="modules"),
    ),
    # Module router
    path(
        "modules/<int:id>/",
        include((module_router.urls, "items"), namespace="items"),
    ),
    # Path router
    path(
        "paths/<int:id>/",
        include((path_router.urls, "courses"), namespace="courses"),
    ),
]
