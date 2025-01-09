""" URLConf for bayt_al_hikmah """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bayt_al_hikmah.answers.views import AnswerViewSet
from bayt_al_hikmah.assignments.views import AssignmentViewSet
from bayt_al_hikmah.categories.views import CategoryViewSet
from bayt_al_hikmah.courses.views import CourseViewSet
from bayt_al_hikmah.departments.views import DepartmentViewSet
from bayt_al_hikmah.enrollments.views import EnrollmentViewSet
from bayt_al_hikmah.faculties.views import FacultyViewSet
from bayt_al_hikmah.items.views import ItemViewSet
from bayt_al_hikmah.lessons.views import LessonViewSet
from bayt_al_hikmah.modules.views import ModuleViewSet
from bayt_al_hikmah.notifications.views import NotificationViewSet
from bayt_al_hikmah.questions.views import QuestionViewSet
from bayt_al_hikmah.reviews.views import ReviewViewSet
from bayt_al_hikmah.specializations.views import SpecializationViewSet
from bayt_al_hikmah.submissions.views import SubmissionViewSet
from bayt_al_hikmah.tags.views import TagViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("answers", AnswerViewSet, "answer")
router.register("assignments", AssignmentViewSet, "assignment")
router.register("categories", CategoryViewSet, "category")
router.register("courses", CourseViewSet, "course")
router.register("departments", DepartmentViewSet, "department")
router.register("enrollments", EnrollmentViewSet, "enrollment")
router.register("faculties", FacultyViewSet, "faculty")
router.register("items", ItemViewSet, "item")
router.register("lessons", LessonViewSet, "lesson")
router.register("modules", ModuleViewSet, "module")
router.register("notifications", NotificationViewSet, "notification")
router.register("questions", QuestionViewSet, "question")
router.register("reviews", ReviewViewSet, "review")
router.register("specializations", SpecializationViewSet, "specialization")
router.register("submissions", SubmissionViewSet, "submission")
router.register("tags", TagViewSet, "tag")


urlpatterns = [
    path("", include(router.urls)),
]
