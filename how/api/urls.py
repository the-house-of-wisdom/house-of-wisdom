"""URL Configuration for how.api"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

from how.api import views
from how.api.viewsets.answers import AnswerViewSet, QuestionAnswers
from how.api.viewsets.assignments import AssignmentViewSet, LessonAssignments
from how.api.viewsets.categories import CategoryViewSet
from how.api.viewsets.courses import CourseViewSet
from how.api.viewsets.enrollments import CourseEnrollments, EnrollmentViewSet
from how.api.viewsets.items import ItemViewSet, LessonItems
from how.api.viewsets.lessons import LessonViewSet, ModuleLessons
from how.api.viewsets.modules import CourseModules, ModuleViewSet
from how.api.viewsets.notifications import NotificationViewSet
from how.api.viewsets.paths import PathViewSet
from how.api.viewsets.posts import CoursePosts, PostViewSet
from how.api.viewsets.questions import AssignmentQuestions, QuestionViewSet
from how.api.viewsets.reviews import CourseReviews, ReviewViewSet
from how.api.viewsets.submissions import AssignmentSubmissions, SubmissionViewSet
from how.api.viewsets.users import UserViewSet

# Create your URLConf here.
router = DefaultRouter()
router.register("answers", AnswerViewSet, "answer")
router.register("enrollments", EnrollmentViewSet, "enrollment")
router.register("notifications", NotificationViewSet, "notification")
router.register("questions", QuestionViewSet, "question")
router.register("reviews", ReviewViewSet, "review")
router.register("submissions", SubmissionViewSet, "submission")
router.register("users", UserViewSet, "user")

# Wagtail APIs
api_router = WagtailAPIRouter("wagtail-api")
# H.O.W Wagtail APIS
api_router.register_endpoint("assignments", AssignmentViewSet)
api_router.register_endpoint("categories", CategoryViewSet)
api_router.register_endpoint("courses", CourseViewSet)
api_router.register_endpoint("items", ItemViewSet)
api_router.register_endpoint("lessons", LessonViewSet)
api_router.register_endpoint("modules", ModuleViewSet)
api_router.register_endpoint("paths", PathViewSet)
api_router.register_endpoint("posts", PostViewSet)
# Built-in Wagtail APIS
api_router.register_endpoint("pages", PagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)

# Sub-routers
course_router = DefaultRouter(trailing_slash=False)
course_router.APIRootView = views.CourseInstanceAPI
course_router.register("enrollments", CourseEnrollments, "enrollment")
course_router.register("posts", CoursePosts, "post")
course_router.register("modules", CourseModules, "module")
course_router.register("reviews", CourseReviews, "review")

module_router = DefaultRouter(trailing_slash=False)
module_router.APIRootView = views.ModuleInstanceAPI
module_router.register("lessons", ModuleLessons, "lesson")

lesson_router = DefaultRouter(trailing_slash=False)
lesson_router.APIRootView = views.LessonInstanceAPI
lesson_router.register("assignments", LessonAssignments, "assignment")
lesson_router.register("items", LessonItems, "item")

assignment_router = DefaultRouter(trailing_slash=False)
assignment_router.APIRootView = views.AssignmentInstanceAPI
assignment_router.register("questions", AssignmentQuestions, "question")
assignment_router.register("submissions", AssignmentSubmissions, "submission")

question_router = DefaultRouter(trailing_slash=False)
question_router.APIRootView = views.QuestionInstanceAPI
question_router.register("answers", QuestionAnswers, "answer")


urlpatterns = [
    path("", include(router.urls)),
    path("", api_router.urls),
]
