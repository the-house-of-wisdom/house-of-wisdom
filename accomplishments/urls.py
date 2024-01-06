""" URLConf for learn.accomplishments """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from learn.accomplishments.views import AccomplishmentViewSet


# Create your patterns here.
router = DefaultRouter(trailing_slash=False)
router.register("accomplishments", AccomplishmentViewSet, "accomplishment")

urlpatterns = [
    path("", include(router.urls)),
]
