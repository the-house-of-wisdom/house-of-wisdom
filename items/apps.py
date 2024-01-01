""" AppConf for learn.items """


from django.apps import AppConfig


# Create your config here.
class ItemConfig(AppConfig):
    """App configuration for learn.items"""

    name = "learn.items"
    default_auto_field = "django.db.models.BigAutoField"
