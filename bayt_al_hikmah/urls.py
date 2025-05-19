"""URLConf for bayt_al_hikmah"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet


from bayt_al_hikmah.answers.views import AnswerViewSet
from bayt_al_hikmah.assignments.views import AssignmentViewSet
from bayt_al_hikmah.categories.views import CategoryViewSet
from bayt_al_hikmah.paths.views import PathViewSet
from bayt_al_hikmah.courses.views import CourseViewSet
from bayt_al_hikmah.enrollments.views import EnrollmentViewSet
from bayt_al_hikmah.items.views import ItemViewSet
from bayt_al_hikmah.lessons.views import LessonViewSet
from bayt_al_hikmah.modules.views import ModuleViewSet
from bayt_al_hikmah.notifications.views import NotificationViewSet
from bayt_al_hikmah.questions.views import QuestionViewSet
from bayt_al_hikmah.reviews.views import ReviewViewSet
from bayt_al_hikmah.submissions.views import SubmissionViewSet
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
router.register("modules", ModuleViewSet, "module")
router.register("lessons", LessonViewSet, "lesson")
router.register("items", ItemViewSet, "item")
router.register("assignments", AssignmentViewSet, "assignment")
router.register("questions", QuestionViewSet, "question")
router.register("answers", AnswerViewSet, "answer")
router.register("submissions", SubmissionViewSet, "submission")
router.register("notifications", NotificationViewSet, "notification")

# Wagtail API endpoints
api_router = WagtailAPIRouter("wagtail_api")
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("cms/", api_router.urls),
]
