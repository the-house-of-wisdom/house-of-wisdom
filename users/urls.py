""" URLConf for learn.users """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.users.views import UserViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, "user")

urlpatterns = [
    path("", include(router.urls)),
]
