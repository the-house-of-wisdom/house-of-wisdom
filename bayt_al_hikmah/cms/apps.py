"""AppConf for bayt_al_hikmah.cms"""

from django.apps import AppConfig
from django.db.models import ForeignKey


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for bayt_al_hikmah.cms"""

    name = "bayt_al_hikmah.cms"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        from wagtail.admin.forms.models import register_form_field_override
        from .widgets import CourseChooserWidget

        register_form_field_override(
            ForeignKey, to="courses.Course", override={"widget": CourseChooserWidget}
        )
        return super().ready()
