"""URLConf for bayt_al_hikmah"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

from bayt_al_hikmah.answers.views import AnswerViewSet, QuestionAnswersVS
from bayt_al_hikmah.assignments.views import AssignmentViewSet, LessonAssignmentsVS
from bayt_al_hikmah.categories.views import CategoryViewSet
from bayt_al_hikmah.paths.views import PathViewSet
from bayt_al_hikmah.courses.views import CourseViewSet
from bayt_al_hikmah.enrollments.views import CourseEnrollmentsVS, EnrollmentViewSet
from bayt_al_hikmah.items.views import ItemViewSet, LessonItemsVS
from bayt_al_hikmah.lessons.views import LessonViewSet, ModuleLessonsVS
from bayt_al_hikmah.modules.views import CourseModulesViewSet, ModuleVS
from bayt_al_hikmah.notifications.views import NotificationViewSet
from bayt_al_hikmah.questions.views import AssignmentQuestionsVS, QuestionViewSet
from bayt_al_hikmah.reviews.views import CourseReviewsVS, ReviewViewSet
from bayt_al_hikmah.submissions.views import AssignmentSubmissionsVS, SubmissionViewSet
from bayt_al_hikmah.tags.views import TagViewSet
from bayt_al_hikmah.users.views import UserViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, "user")
router.register("tags", TagViewSet, "tag")
router.register("categories", CategoryViewSet, "category")
router.register("paths", PathViewSet, "path")
router.register("courses", CourseViewSet, "course")
router.register("enrollments", EnrollmentViewSet, "enrollment")
router.register("reviews", ReviewViewSet, "review")
router.register("modules", ModuleVS, "module")
router.register("lessons", LessonViewSet, "lesson")
router.register("items", ItemViewSet, "item")
router.register("assignments", AssignmentViewSet, "assignment")
router.register("questions", QuestionViewSet, "question")
router.register("answers", AnswerViewSet, "answer")
router.register("submissions", SubmissionViewSet, "submission")
router.register("notifications", NotificationViewSet, "notification")

# Sub-routers
course_router = DefaultRouter(trailing_slash=False)
course_router.register("enrollments", CourseEnrollmentsVS, "enrollment")
course_router.register("modules", CourseModulesViewSet, "module")
course_router.register("reviews", CourseReviewsVS, "review")

module_router = DefaultRouter(trailing_slash=False)
module_router.register("lessons", ModuleLessonsVS, "lesson")

lesson_router = DefaultRouter(trailing_slash=False)
lesson_router.register("assignments", LessonAssignmentsVS, "assignment")
lesson_router.register("items", LessonItemsVS, "item")

assignment_router = DefaultRouter(trailing_slash=False)
assignment_router.register("questions", AssignmentQuestionsVS, "question")
assignment_router.register("submissions", AssignmentSubmissionsVS, "submission")

question_router = DefaultRouter(trailing_slash=False)
question_router.register("answers", QuestionAnswersVS, "answer")


# Wagtail API endpoints
api_router = WagtailAPIRouter("wagtail_api")
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", api_router.urls),
    # Sub-router patterns
    path("courses/<int:course_id>/", include(course_router.urls)),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/", include(module_router.urls)
    ),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/lessons/<int:lesson_id>/",
        include(lesson_router.urls),
    ),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/lessons/<int:lesson_id>/assignments/<int:assignment_id>/",
        include(assignment_router.urls),
    ),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/lessons/<int:lesson_id>/assignments/<int:assignment_id>/questions/<int:question_id>/",
        include(question_router.urls),
    ),
]
