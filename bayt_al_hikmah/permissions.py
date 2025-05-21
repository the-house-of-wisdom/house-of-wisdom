"""Custom API access permissions"""

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.questions.models import Question


# Create your permissions here.
class DenyAll(BasePermission):
    """Deny all requests"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return False

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return False


class IsAccountOwner(BasePermission):
    """Check if the user is the owner of the account"""

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return request.user == obj


class IsInstructor(BasePermission):
    """Check if the user is an instructor"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return request.user.is_instructor


class IsOwner(BasePermission):
    """Check if the user is the owner of the obj"""

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return request.user.id == obj.user_id


class IsModelOwner(BasePermission):
    """Base class that checks if the user is owner of the obj"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return Course.objects.filter(
            id=view.kwargs["course_id"], user_id=request.user.id
        ).exists()

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return Course.objects.filter(
            id=view.kwargs["course_id"], user_id=request.user.id
        ).exists()


class IsModuleOwner(IsModelOwner):
    """Check if the user is the owner of the Module"""


class IsLessonOwner(IsModelOwner):
    """Check if the user is the owner of the Lesson"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return Module.objects.filter(
            id=view.kwargs["module_id"],
            course_id=view.kwargs["course_id"],
            course__user_id=request.user.id,
        ).exists()


class IsAIOwner(IsModelOwner):
    """Check if the user is the owner of the Assignment or Item"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return Lesson.objects.filter(
            id=view.kwargs["lesson_id"],
            module_id=view.kwargs["module_id"],
            module__course_id=view.kwargs["course_id"],
            module__course__user_id=request.user.id,
        ).exists()


class IsAssignmentOwner(IsAIOwner):
    """Check if the user is the owner of the Assignment"""


class IsItemOwner(IsAIOwner):
    """Check if the user is the owner of the Item"""


class IsQuestionOwner(IsModelOwner):
    """Check if the user is the owner of the Question"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return Assignment.objects.filter(
            id=view.kwargs["assignment_id"],
            lesson_id=view.kwargs["lesson_id"],
            lesson__module_id=view.kwargs["module_id"],
            lesson__module__course_id=view.kwargs["course_id"],
            lesson__module__course__user_id=request.user.id,
        ).exists()


class IsAnswerOwner(IsModelOwner):
    """Check if the user is the owner of the Answer"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return Question.objects.filter(
            id=view.kwargs["question_id"],
            assignment_id=view.kwargs["assignment_id"],
            assignment__lesson_id=view.kwargs["lesson_id"],
            assignment__lesson__module_id=view.kwargs["module_id"],
            assignment__lesson__module__course_id=view.kwargs["course_id"],
            assignment__lesson__module__course__user_id=request.user.id,
        ).exists()
