"""AppConf for how.apps.items"""

from django.apps import AppConfig


# Create your config here.
class ItemsConfig(AppConfig):
    """App configuration for how.apps.items"""

    name = "how.apps.items"
    default_auto_field = "django.db.models.BigAutoField"
