""" URLConf for learn """

from django.urls import path, include


# Create your patterns here.
urlpatterns = [
    path("", include("learn.accomplishments.urls")),
    path("", include("learn.courses.urls")),
    path("", include("learn.items.urls")),
    path("", include("learn.modules.urls")),
    path("", include("learn.projects.urls")),
    path("", include("learn.specializations.urls")),
]
