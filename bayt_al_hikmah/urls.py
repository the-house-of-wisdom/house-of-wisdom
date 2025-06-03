"""URLConf for bayt_al_hikmah"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

from bayt_al_hikmah import views
from bayt_al_hikmah.answers.views import AnswerViewSet, QuestionAnswers
from bayt_al_hikmah.assignments.views import AssignmentViewSet, LessonAssignments
from bayt_al_hikmah.blog.views import ArticleViewSet
from bayt_al_hikmah.categories.views import CategoryViewSet
from bayt_al_hikmah.paths.views import PathViewSet
from bayt_al_hikmah.courses.views import CourseViewSet
from bayt_al_hikmah.enrollments.views import CourseEnrollments, EnrollmentViewSet
from bayt_al_hikmah.items.views import ItemViewSet, LessonItems
from bayt_al_hikmah.lessons.views import LessonViewSet, ModuleLessons
from bayt_al_hikmah.modules.views import CourseModules, ModuleViewSet
from bayt_al_hikmah.posts.views import CoursePosts, PostViewSet
from bayt_al_hikmah.questions.views import AssignmentQuestions, QuestionViewSet
from bayt_al_hikmah.reviews.views import CourseReviews, ReviewViewSet
from bayt_al_hikmah.submissions.views import AssignmentSubmissions, SubmissionViewSet
from bayt_al_hikmah.users.views import UserViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.APIRootView = views.HouseOfWisdomAPI
router.register("articles", ArticleViewSet, "article")
router.register("users", UserViewSet, "user")
router.register("categories", CategoryViewSet, "category")
router.register("paths", PathViewSet, "path")
router.register("courses", CourseViewSet, "course")
router.register("enrollments", EnrollmentViewSet, "enrollment")
router.register("posts", PostViewSet, "post")
router.register("modules", ModuleViewSet, "module")
router.register("reviews", ReviewViewSet, "review")
router.register("lessons", LessonViewSet, "lesson")
router.register("items", ItemViewSet, "item")
router.register("assignments", AssignmentViewSet, "assignment")
router.register("questions", QuestionViewSet, "question")
router.register("answers", AnswerViewSet, "answer")
router.register("submissions", SubmissionViewSet, "submission")

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


# NOTE: Check if it is mandatory to include Wagtail API
# Wagtail API endpoints
wagtail_router = WagtailAPIRouter("wagtail_api")
wagtail_router.register_endpoint("documents", DocumentsAPIViewSet)
wagtail_router.register_endpoint("images", ImagesAPIViewSet)
wagtail_router.register_endpoint("pages", PagesAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", wagtail_router.urls),
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
