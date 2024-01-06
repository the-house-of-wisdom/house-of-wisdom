""" AppConf for learn.projects """


from django.apps import AppConfig


# Create your config here.
class ProjectsConfig(AppConfig):
    """App configuration for learn.projects"""

    name = "learn.projects"
    default_auto_field = "django.db.models.BigAutoField"
