"""AppConf for how.users"""

from django.apps import AppConfig


# Create your config here.
class UsersConfig(AppConfig):
    """App configuration for how.users"""

    name = "how.users"
    default_auto_field = "django.db.models.BigAutoField"
