""" AppConf for learn.courses """


from django.apps import AppConfig


# Create your config here.
class CoursesConfig(AppConfig):
    """App configuration for learn.courses"""

    name = "learn.courses"
    default_auto_field = "django.db.models.BigAutoField"
