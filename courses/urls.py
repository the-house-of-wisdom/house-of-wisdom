""" URLConf for learn.courses """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.courses.views import CourseViewSet, CourseImageView


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("courses", CourseViewSet, "course")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("courses/<int:pk>/image", CourseImageView.as_view()),
    path(
        "courses/<int:id>/",
        include((sub_router.urls, "courses"), namespace="courses"),
    ),
]
