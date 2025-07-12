"""AppConf for how.apps.posts"""

from django.apps import AppConfig


# Create your config here.
class PostsConfig(AppConfig):
    """App configuration for how.apps.posts"""

    name = "how.apps.posts"
    default_auto_field = "django.db.models.BigAutoField"
