"""URLConf for bayt_al_hikmah.ui"""

from django.urls import path

from bayt_al_hikmah.ui import views


# Create your URLConf here.
app_name = "ui"


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
