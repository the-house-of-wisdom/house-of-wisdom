"""AppConf for how.blog"""

from django.apps import AppConfig


# Create your config here.
class BlogConfig(AppConfig):
    """App configuration for how.blog"""

    name = "how.blog"
    default_auto_field = "django.db.models.BigAutoField"
