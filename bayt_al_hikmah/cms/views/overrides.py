"""Overridden views that add filtering"""

from wagtail.admin.views import generic

from bayt_al_hikmah.ui import mixins


# Create your views here.
# Courses
class UserCreateView(mixins.OwnerMixin, generic.CreateView):
    """Adds the owner of the object automatically"""


class UserCoursesView(mixins.UserFilterMixin, generic.IndexView):
    """Filter the queryset by user to display only courses owned by that user"""


class UserCoursesEditView(mixins.UserFilterMixin, generic.EditView):
    """Filter the queryset by user to edit only courses owned by that user"""


class UserCoursesDeleteView(mixins.UserFilterMixin, generic.DeleteView):
    """Filter the queryset by user to delete only courses owned by that user"""


class UserCoursesHistoryView(mixins.UserFilterMixin, generic.HistoryView):
    """Filter the queryset by user to view only courses owned by that user"""


class UserCoursesUsageView(mixins.UserFilterMixin, generic.UsageView):
    """Filter the queryset by user to view only courses owned by that user"""


# Modules
class UserModulesView(mixins.UserModulesMixin, generic.IndexView):
    """Filter the queryset by user to display only modules owned by that user"""


class UserModulesEditView(mixins.UserModulesMixin, generic.EditView):
    """Filter the queryset by user to edit only modules owned by that user"""


class UserModulesDeleteView(mixins.UserModulesMixin, generic.DeleteView):
    """Filter the queryset by user to delete only modules owned by that user"""


class UserModulesHistoryView(mixins.UserModulesMixin, generic.HistoryView):
    """Filter the queryset by user to view only modules owned by that user"""


class UserModulesUsageView(mixins.UserModulesMixin, generic.UsageView):
    """Filter the queryset by user to view only modules owned by that user"""


# Lessons
class UserLessonsView(mixins.UserLessonsMixin, generic.IndexView):
    """Filter the queryset by user to display only lessons owned by that user"""


class UserLessonsEditView(mixins.UserLessonsMixin, generic.EditView):
    """Filter the queryset by user to edit only lessons owned by that user"""


class UserLessonsDeleteView(mixins.UserLessonsMixin, generic.DeleteView):
    """Filter the queryset by user to delete only lessons owned by that user"""


class UserLessonsHistoryView(mixins.UserLessonsMixin, generic.HistoryView):
    """Filter the queryset by user to view only lessons owned by that user"""


class UserLessonsUsageView(mixins.UserLessonsMixin, generic.UsageView):
    """Filter the queryset by user to view only lessons owned by that user"""


# Assignments & Items
class UserAIView(mixins.UserAIMixin, generic.IndexView):
    """Filter the queryset by user to display only assignments and items owned by that user"""


class UserAIEditView(mixins.UserAIMixin, generic.EditView):
    """Filter the queryset by user to edit only assignments and items owned by that user"""


class UserAIDeleteView(mixins.UserAIMixin, generic.DeleteView):
    """Filter the queryset by user to delete only assignments and items owned by that user"""


class UserAIHistoryView(mixins.UserAIMixin, generic.HistoryView):
    """Filter the queryset by user to view only assignments and items owned by that user"""


class UserAIUsageView(mixins.UserAIMixin, generic.UsageView):
    """Filter the queryset by user to view only assignments and items owned by that user"""


# Questions
class UserQuestionsView(mixins.UserQuestionsMixin, generic.IndexView):
    """Filter the queryset by user to display only questions owned by that user"""


class UserQuestionsEditView(mixins.UserQuestionsMixin, generic.EditView):
    """Filter the queryset by user to edit only questions owned by that user"""


class UserQuestionsDeleteView(mixins.UserQuestionsMixin, generic.DeleteView):
    """Filter the queryset by user to delete only questions owned by that user"""


class UserQuestionsHistoryView(mixins.UserQuestionsMixin, generic.HistoryView):
    """Filter the queryset by user to view only questions owned by that user"""


class UserQuestionsUsageView(mixins.UserQuestionsMixin, generic.UsageView):
    """Filter the queryset by user to view only questions owned by that user"""


# Answers
class UserAnswersView(mixins.UserAnswersMixin, generic.IndexView):
    """Filter the queryset by user to display only answers owned by that user"""


class UserAnswersEditView(mixins.UserAnswersMixin, generic.EditView):
    """Filter the queryset by user to edit only answers owned by that user"""


class UserAnswersDeleteView(mixins.UserAnswersMixin, generic.DeleteView):
    """Filter the queryset by user to delete only answers owned by that user"""


class UserAnswersHistoryView(mixins.UserAnswersMixin, generic.HistoryView):
    """Filter the queryset by user to view only answers owned by that user"""


class UserAnswersUsageView(mixins.UserAnswersMixin, generic.UsageView):
    """Filter the queryset by user to view only answers owned by that user"""
