""" URLConf for learn """


from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path(
        "/<int:id>/",
        include((sub_router.urls, ""), namespace=""),
    ),
    path("", include("learn.accomplishments")),
    path("", include("learn.courses")),
    path("", include("learn.items")),
    path("", include("learn.modules")),
    path("", include("learn.projects")),
    path("", include("learn.specializations")),
]
