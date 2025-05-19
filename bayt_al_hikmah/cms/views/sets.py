"""ViewSets"""

from wagtail.admin.viewsets.model import ModelViewSet

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.cms.views import overrides
from bayt_al_hikmah.collections.models import Collection
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.questions.models import Question


# Create your viewsets here.
class CollectionViewSet(ModelViewSet):
    """Wagtail Collection ViewSet"""

    model = Collection
    index_view_class = overrides.UserCoursesView
    add_view_class = overrides.UserCreateView
    edit_view_class = overrides.UserCoursesEditView
    delete_view_class = overrides.UserCoursesDeleteView
    history_view_class = overrides.UserCoursesHistoryView
    usage_view_class = overrides.UserCoursesUsageView
    form_fields = [
        "category",
        "image",
        "name",
        "headline",
        "description",
        "tags",
        "courses",
    ]
    list_display = ["category", "name"]
    list_filter = ["category", "name"]
    icon = "user"
    add_to_admin_menu = True


class CourseViewSet(ModelViewSet):
    """Wagtail Course ViewSet"""

    model = Course
    index_view_class = overrides.UserCoursesView
    add_view_class = overrides.UserCreateView
    edit_view_class = overrides.UserCoursesEditView
    delete_view_class = overrides.UserCoursesDeleteView
    history_view_class = overrides.UserCoursesHistoryView
    usage_view_class = overrides.UserCoursesUsageView
    form_fields = ["category", "image", "name", "headline", "description", "tags"]
    list_display = ["category", "name"]
    list_filter = ["category", "name"]
    icon = "user"


class ModuleViewSet(ModelViewSet):
    """Wagtail Module ViewSet"""

    model = Module
    index_view_class = overrides.UserModulesView
    edit_view_class = overrides.UserModulesEditView
    delete_view_class = overrides.UserModulesDeleteView
    history_view_class = overrides.UserModulesHistoryView
    usage_view_class = overrides.UserModulesUsageView
    form_fields = ["course", "title", "description"]
    list_display = ["course", "title"]
    list_filter = ["course"]
    icon = "user"


class LessonViewSet(ModelViewSet):
    """Wagtail Lesson ViewSet"""

    model = Lesson
    index_view_class = overrides.UserLessonsView
    edit_view_class = overrides.UserLessonsEditView
    delete_view_class = overrides.UserLessonsDeleteView
    history_view_class = overrides.UserLessonsHistoryView
    usage_view_class = overrides.UserLessonsUsageView
    form_fields = ["module", "name", "description"]
    list_display = ["module", "name"]
    list_filter = ["module"]
    icon = "user"


class AssignmentViewSet(ModelViewSet):
    """Wagtail Assignment ViewSet"""

    model = Assignment
    index_view_class = overrides.UserAIView
    edit_view_class = overrides.UserAIEditView
    delete_view_class = overrides.UserAIDeleteView
    history_view_class = overrides.UserAIHistoryView
    usage_view_class = overrides.UserAIUsageView
    form_fields = [
        "lesson",
        "is_auto_graded",
        "title",
        "description",
        "question_count",
        "min_percentage",
        "content",
    ]
    list_display = form_fields = ["lesson", "is_auto_graded", "title"]
    list_filter = form_fields = [
        "lesson",
        "is_auto_graded",
        "question_count",
        "min_percentage",
    ]
    icon = "user"


class ItemViewSet(AssignmentViewSet):
    """Wagtail Item ViewSet"""

    model = Item
    form_fields = ["lesson", "type", "title", "content"]
    list_display = ["lesson", "title", "type"]
    list_filter = ["lesson", "type"]
    icon = "user"


class QuestionViewSet(ModelViewSet):
    """Wagtail Question ViewSet"""

    model = Question
    index_view_class = overrides.UserQuestionsView
    edit_view_class = overrides.UserQuestionsEditView
    delete_view_class = overrides.UserQuestionsDeleteView
    history_view_class = overrides.UserQuestionsHistoryView
    usage_view_class = overrides.UserQuestionsUsageView
    form_fields = ["assignment", "type", "text"]
    list_display = ["assignment", "type", "text"]
    list_filter = ["assignment", "type"]
    icon = "user"


class AnswerViewSet(ModelViewSet):
    """Wagtail Answer ViewSet"""

    model = Answer
    index_view_class = overrides.UserAnswersView
    edit_view_class = overrides.UserAnswersEditView
    delete_view_class = overrides.UserAnswersDeleteView
    history_view_class = overrides.UserAnswersHistoryView
    usage_view_class = overrides.UserAnswersUsageView
    form_fields = ["question", "is_correct", "text", "description"]
    list_display = ["question", "is_correct", "text"]
    list_filter = ["question", "is_correct"]
    icon = "user"


viewsets = {
    "courses": CourseViewSet("courses"),
    "modules": ModuleViewSet("modules"),
    "lessons": LessonViewSet("lessons"),
    "assignments": AssignmentViewSet("assignments"),
    "questions": QuestionViewSet("questions"),
    "answers": AnswerViewSet("answers"),
}
