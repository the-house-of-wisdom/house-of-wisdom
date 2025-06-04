"""AppConf for how.posts"""

from django.apps import AppConfig


# Create your config here.
class PostsConfig(AppConfig):
    """App configuration for how.posts"""

    name = "how.posts"
    default_auto_field = "django.db.models.BigAutoField"
