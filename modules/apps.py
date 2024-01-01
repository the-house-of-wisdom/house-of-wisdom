""" AppConf for learn.modules """


from django.apps import AppConfig


# Create your config here.
class ModuleConfig(AppConfig):
    """App configuration for learn.modules"""

    name = "learn.modules"
    default_auto_field = "django.db.models.BigAutoField"
