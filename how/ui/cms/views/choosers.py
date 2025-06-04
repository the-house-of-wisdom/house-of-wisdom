"""Chooser ViewSets"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.viewsets.chooser import ChooserViewSet


# Create your chooser viewsets here.
class CategoryChooserViewSet(ChooserViewSet):
    """Category chooser view set"""

    icon = "folder-inverse"
    model = "categories.Category"
    choose_one_text = _("Choose a Category")
    edit_item_text = _("Edit this Category")
    choose_another_text = _("Choose another Category")
    form_fields = ["title", "description"]


class PathChooserViewSet(ChooserViewSet):
    """Path chooser view set"""

    icon = "folder-open-1"
    model = "paths.LearningPath"
    choose_one_text = _("Choose a Learning Path")
    edit_item_text = _("Edit this Learning Path")
    choose_another_text = _("Choose another Learning Path")


class CourseChooserViewSet(ChooserViewSet):
    """Course chooser view set"""

    icon = "folder-open-inverse"
    model = "courses.Course"
    choose_one_text = _("Choose a Course")
    edit_item_text = _("Edit this Course")
    choose_another_text = _("Choose another Course")


class ModuleChooserViewSet(ChooserViewSet):
    """Module chooser view set"""

    icon = "folder"
    model = "modules.Module"
    choose_one_text = _("Choose a Module")
    edit_item_text = _("Edit this Module")
    choose_another_text = _("Choose another Module")


class LessonChooserViewSet(ChooserViewSet):
    """Lesson chooser view set"""

    icon = "doc-empty"
    model = "lessons.Lesson"
    choose_one_text = _("Choose a Lesson")
    edit_item_text = _("Edit this Lesson")
    choose_another_text = _("Choose another Lesson")


class AssignmentChooserViewSet(ChooserViewSet):
    """Assignment chooser view set"""

    icon = "bars"
    model = "assignments.Assignment"
    choose_one_text = _("Choose a Assignment")
    edit_item_text = _("Edit this Assignment")
    choose_another_text = _("Choose another Assignment")


class ItemChooserViewSet(ChooserViewSet):
    """Item chooser view set"""

    icon = "doc-full-inverse"
    model = "items.Item"
    choose_one_text = _("Choose a Item")
    edit_item_text = _("Edit this Item")
    choose_another_text = _("Choose another Item")


class QuestionChooserViewSet(ChooserViewSet):
    """Question chooser view set"""

    icon = "circle-check"
    model = "questions.Question"
    choose_one_text = _("Choose a Question")
    edit_item_text = _("Edit this Question")
    choose_another_text = _("Choose another Question")


viewsets = {
    "categories": CategoryChooserViewSet("category_chooser"),
    "paths": PathChooserViewSet("path_chooser"),
    "courses": CourseChooserViewSet("course_chooser"),
    "modules": ModuleChooserViewSet("module_chooser"),
    "lessons": LessonChooserViewSet("lesson_chooser"),
    "assignments": AssignmentChooserViewSet("assignment_chooser"),
    "items": ItemChooserViewSet("item_chooser"),
    "questions": QuestionChooserViewSet("question_chooser"),
}
