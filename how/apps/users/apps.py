"""AppConf for how.apps.users"""

from django.apps import AppConfig


# Create your config here.
class UsersConfig(AppConfig):
    """App configuration for how.apps.users"""

    name = "how.apps.users"
    default_auto_field = "django.db.models.BigAutoField"
