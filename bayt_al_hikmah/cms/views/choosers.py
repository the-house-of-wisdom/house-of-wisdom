"""Chooser ViewSets"""

from wagtail.admin.viewsets.chooser import ChooserViewSet


# Create your chooser viewsets here.
class CategoryChooserViewSet(ChooserViewSet):
    """Category chooser view set"""

    icon = "user"
    model = "categories.Category"
    choose_one_text = "Choose a Category"
    edit_item_text = "Edit this Category"
    choose_another_text = "Choose another Category"
    form_fields = ["name", "headline"]


class TagChooserViewSet(ChooserViewSet):
    """Tag chooser view set"""

    icon = "user"
    model = "tags.Tag"
    choose_one_text = "Choose a Tag"
    edit_item_text = "Edit this Tag"
    choose_another_text = "Choose another Tag"
    form_fields = ["name", "headline"]


class PathChooserViewSet(ChooserViewSet):
    """Path chooser view set"""

    icon = "user"
    model = "paths.Path"
    choose_one_text = "Choose a Learning Path"
    edit_item_text = "Edit this Learning Path"
    choose_another_text = "Choose another Learning Path"
    form_fields = ["name", "headline"]


class CourseChooserViewSet(ChooserViewSet):
    """Course chooser view set"""

    icon = "user"
    model = "courses.Course"
    choose_one_text = "Choose a Course"
    edit_item_text = "Edit this Course"
    choose_another_text = "Choose another Course"
    form_fields = ["name", "headline"]


class ModuleChooserViewSet(ChooserViewSet):
    """Module chooser view set"""

    icon = "user"
    model = "modules.Module"
    choose_one_text = "Choose a Module"
    edit_item_text = "Edit this Module"
    choose_another_text = "Choose another Module"
    form_fields = ["name", "headline"]


class LessonChooserViewSet(ChooserViewSet):
    """Lesson chooser view set"""

    icon = "user"
    model = "lessons.Lesson"
    choose_one_text = "Choose a Lesson"
    edit_item_text = "Edit this Lesson"
    choose_another_text = "Choose another Lesson"
    form_fields = ["name", "headline"]


class AssignmentChooserViewSet(ChooserViewSet):
    """Assignment chooser view set"""

    icon = "user"
    model = "assignments.Assignment"
    choose_one_text = "Choose a Assignment"
    edit_item_text = "Edit this Assignment"
    choose_another_text = "Choose another Assignment"
    form_fields = ["name", "headline"]


class ItemChooserViewSet(ChooserViewSet):
    """Item chooser view set"""

    icon = "user"
    model = "items.Item"
    choose_one_text = "Choose a Item"
    edit_item_text = "Edit this Item"
    choose_another_text = "Choose another Item"
    form_fields = ["name", "headline"]


class QuestionChooserViewSet(ChooserViewSet):
    """Question chooser view set"""

    icon = "user"
    model = "questions.Question"
    choose_one_text = "Choose a Question"
    edit_item_text = "Edit this Question"
    choose_another_text = "Choose another Question"
    form_fields = ["name", "headline"]


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
