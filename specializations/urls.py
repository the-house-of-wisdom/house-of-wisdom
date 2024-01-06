""" URLConf for learn.specializations """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.specializations.views import SpecializationViewSet, SpecializationImageView


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("specializations", SpecializationViewSet, "specialization")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("specializations/<int:pk>/image", SpecializationImageView.as_view()),
    path(
        "specializations/<int:id>/",
        include((sub_router.urls, "specializations"), namespace="specializations"),
    ),
]
