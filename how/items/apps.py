"""AppConf for how.items"""

from django.apps import AppConfig


# Create your config here.
class ItemsConfig(AppConfig):
    """App configuration for how.items"""

    name = "how.items"
    default_auto_field = "django.db.models.BigAutoField"
