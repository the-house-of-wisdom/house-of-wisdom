""" URLConf for learn.instructors """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.instructors.views import InstructorViewSet, InstructorImageView


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("instructors", InstructorViewSet, "instructor")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("instructors/<int:pk>/image", InstructorImageView.as_view()),
    path(
        "instructors/<int:id>/",
        include((sub_router.urls, "instructors"), namespace="instructors"),
    ),
]
