""" URLConf for learn.enrollments """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.enrollments.views import EnrollmentViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("enrollments", EnrollmentViewSet, "enrollment")

urlpatterns = [
    path("", include(router.urls)),
]
