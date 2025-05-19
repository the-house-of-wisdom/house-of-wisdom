"""Chooser ViewSets"""

from wagtail.admin.viewsets.chooser import ChooserViewSet


# Create your chooser viewsets here.
class CourseChooserViewSet(ChooserViewSet):
    """Course chooser view set"""

    icon = "user"
    model = "courses.Course"
    choose_one_text = "Choose a Course"
    edit_item_text = "Edit this Course"
    choose_another_text = "Choose another Course"
    form_fields = ["name", "headline"]


chooser_viewsets = {
    "courses": CourseChooserViewSet("course_chooser"),
}
