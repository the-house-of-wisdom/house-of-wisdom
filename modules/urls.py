""" URLConf for learn.modules """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.modules.views import ModuleViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("modules", ModuleViewSet, "module")

sub_router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path(
        "modules/<int:id>/",
        include((sub_router.urls, "modules"), namespace="modules"),
    ),
]
