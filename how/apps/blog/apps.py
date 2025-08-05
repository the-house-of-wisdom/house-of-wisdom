"""AppConf for how.apps.blog"""

from django.apps import AppConfig


# Create your config here.
class BlogConfig(AppConfig):
    """App configuration for how.apps.blog"""

    name = "how.apps.blog"
    default_auto_field = "django.db.models.BigAutoField"
