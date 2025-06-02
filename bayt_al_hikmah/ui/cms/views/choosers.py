"""Chooser ViewSets"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.viewsets.chooser import ChooserViewSet


# Create your chooser viewsets here.
class CategoryChooserViewSet(ChooserViewSet):
    """Category chooser view set"""

    icon = "user"
    model = "categories.Category"
    choose_one_text = _("Choose a Category")
    edit_item_text = _("Edit this Category")
    choose_another_text = _("Choose another Category")
    form_fields = ["name", "description"]


class TagChooserViewSet(ChooserViewSet):
    """Tag chooser view set"""

    icon = "user"
    model = "tags.Tag"
    choose_one_text = _("Choose a Tag")
    edit_item_text = _("Edit this Tag")
    choose_another_text = _("Choose another Tag")
    form_fields = ["name", "description"]


class PathChooserViewSet(ChooserViewSet):
    """Path chooser view set"""

    icon = "user"
    model = "paths.Path"
    choose_one_text = _("Choose a Learning Path")
    edit_item_text = _("Edit this Learning Path")
    choose_another_text = _("Choose another Learning Path")
    form_fields = [
        "category",
        "image",
        "name",
        "headline",
        "description",
        "duration",
        "prerequisites",
        "tags",
        "courses",
    ]


class CourseChooserViewSet(ChooserViewSet):
    """Course chooser view set"""

    icon = "user"
    model = "courses.Course"
    choose_one_text = _("Choose a Course")
    edit_item_text = _("Edit this Course")
    choose_another_text = _("Choose another Course")
    form_fields = [
        "category",
        "image",
        "name",
        "headline",
        "description",
        "duration",
        "prerequisites",
        "tags",
    ]


class ModuleChooserViewSet(ChooserViewSet):
    """Module chooser view set"""

    icon = "user"
    model = "modules.Module"
    choose_one_text = _("Choose a Module")
    edit_item_text = _("Edit this Module")
    choose_another_text = _("Choose another Module")
    form_fields = ["course", "name", "description"]


class LessonChooserViewSet(ChooserViewSet):
    """Lesson chooser view set"""

    icon = "user"
    model = "lessons.Lesson"
    choose_one_text = _("Choose a Lesson")
    edit_item_text = _("Edit this Lesson")
    choose_another_text = _("Choose another Lesson")
    form_fields = ["module", "name", "description"]


class AssignmentChooserViewSet(ChooserViewSet):
    """Assignment chooser view set"""

    icon = "user"
    model = "assignments.Assignment"
    choose_one_text = _("Choose a Assignment")
    edit_item_text = _("Edit this Assignment")
    choose_another_text = _("Choose another Assignment")
    form_fields = [
        "lesson",
        "type",
        "name",
        "description",
        "question_count",
        "min_percentage",
        "content",
        "is_auto_graded",
    ]


class ItemChooserViewSet(ChooserViewSet):
    """Item chooser view set"""

    icon = "user"
    model = "items.Item"
    choose_one_text = _("Choose a Item")
    edit_item_text = _("Edit this Item")
    choose_another_text = _("Choose another Item")
    form_fields = ["lesson", "name", "description"]


class QuestionChooserViewSet(ChooserViewSet):
    """Question chooser view set"""

    icon = "user"
    model = "questions.Question"
    choose_one_text = _("Choose a Question")
    edit_item_text = _("Edit this Question")
    choose_another_text = _("Choose another Question")
    form_fields = ["assignment", "type", "text"]


viewsets = {
    "categories": CategoryChooserViewSet("category_chooser"),
    "tags": TagChooserViewSet("tag_chooser"),
    "paths": PathChooserViewSet("path_chooser"),
    "courses": CourseChooserViewSet("course_chooser"),
    "modules": ModuleChooserViewSet("module_chooser"),
    "lessons": LessonChooserViewSet("lesson_chooser"),
    "assignments": AssignmentChooserViewSet("assignment_chooser"),
    "items": ItemChooserViewSet("item_chooser"),
    "questions": QuestionChooserViewSet("question_chooser"),
}
