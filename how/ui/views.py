"""Views for how.apps.tags"""

from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query import QuerySet
from django.forms import BaseForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django_filters.views import FilterView
from more_itertools import flatten

from how.apps.assignments.models import Assignment
from how.apps.courses.models import Course
from how.apps.enrollments.models import Enrollment
from how.apps.items.models import Item
from how.apps.lessons.models import Lesson
from how.apps.modules.models import Module
from how.apps.posts.models import Post
from how.apps.reviews.models import Review
from how.apps.submissions.models import Submission
from how.ui import mixins
from how.ui.forms import UserCreateForm

# Create your views here.
User = get_user_model()


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """Profile page"""

    template_name = "registration/profile.html"


class SignupView(SuccessMessageMixin, generic.CreateView):
    """Create a new user"""

    model = User
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("ui:profile")
    success_message = "Your account was created successfully!"


class UserUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    generic.UpdateView,
):
    """Update a user"""

    model = User
    template_name = "registration/edit.html"
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("ui:profile")
    success_message = "Your account was updated successfully!"


class UserDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    generic.DeleteView,
):
    """Delete a user"""

    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("ui:index")
    success_message = "Your account was deleted successfully!"


# Courses
class LearnView(LoginRequiredMixin, generic.TemplateView):
    """My courses"""

    template_name = "ui/learn/index.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """Add extra context"""

        return {
            **super().get_context_data(**kwargs),
            "courses": self.request.user.enrollments.filter(is_completed=False),
            "completed_courses": self.request.user.enrollments.filter(
                is_completed=True
            ),
        }


class CourseDetailView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    generic.DetailView,
):
    """Course details"""

    model = Course
    slug_url_kwarg = "course"
    template_name = "ui/learn/base.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add posts to context"""

        context = super().get_context_data(**kwargs)

        return {**context, "modules": Module.objects.live().child_of(context["course"])}


class CourseGradesView(CourseDetailView):
    """Course graded assignment list"""

    template_name = "ui/learn/content/grades.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add assignments to context"""

        context = super().get_context_data(**kwargs)

        return {
            **context,
            "assignments": Assignment.objects.live()
            .descendant_of(context["course"])
            .filter(is_graded=True),
        }


class CourseReviewsView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    FilterView,
    generic.ListView,
):
    """Course reviews list"""

    model = Review
    paginate_by = 25
    context_object_name = "reviews"
    filterset_fields = ["rating", "sentiment"]
    template_name = "ui/learn/reviews/list.html"

    def get_queryset(self) -> QuerySet[Any]:
        """Filter queryset by course"""

        return super().get_queryset().filter(course__slug=self.kwargs["course"])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add course and modules to context"""

        context = super().get_context_data(**kwargs)

        try:
            course = Course.objects.get(slug=self.kwargs["course"])

            return {
                **context,
                "course": course,
                "modules": Module.objects.live().child_of(course),
            }

        except Course.DoesNotExist:
            return context


class ReviewCreateView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Create reviews"""

    model = Review
    fields = ["rating", "comment"]
    template_name = "ui/learn/reviews/new.html"
    success_message = _("Thanks for reviewing this course")

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """Check if review by user exists to redirect to review update view"""

        try:
            review = Review.objects.get(
                owner=request.user, course__slug=self.kwargs["course"]
            )
            return redirect(
                reverse_lazy(
                    "ui:update_review", args=[self.kwargs["course"], review.pk]
                )
            )

        except Review.DoesNotExist:
            return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("ui:reviews", args=[self.kwargs["course"]])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add course and modules to context"""

        context = super().get_context_data(**kwargs)

        try:
            course = Course.objects.get(slug=self.kwargs["course"])

            return {
                **context,
                "course": course,
                "modules": Module.objects.live().child_of(course),
            }

        except Course.DoesNotExist:
            return context

    def form_valid(self, form: BaseForm) -> HttpResponse:
        """Add owner and course to review"""

        review = form.save(commit=False)
        review.owner = self.request.user

        try:
            review.course = Course.objects.get(slug=self.kwargs["course"])

        except Course.DoesNotExist:
            messages.error(self.request, _("Course does not exists"))
            return redirect(reverse_lazy("ui:learn"))

        return super().form_valid(form)


class ReviewUpdateView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    SuccessMessageMixin,
    mixins.OwnerFilterMixin,
    generic.UpdateView,
):
    """Create reviews"""

    model = Review
    fields = ["rating", "comment"]
    template_name = "ui/learn/reviews/new.html"
    success_message = _("Review updated successfully")

    def get_success_url(self) -> str:
        return reverse_lazy("ui:reviews", args=[self.kwargs["course"]])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add course and modules to context"""

        context = super().get_context_data(**kwargs)

        try:
            course = Course.objects.get(slug=self.kwargs["course"])

            return {
                **context,
                "course": course,
                "modules": Module.objects.live().child_of(course),
            }

        except Course.DoesNotExist:
            return context


class EnrollmentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """Enroll in a course"""

    model = Enrollment
    fields = []
    template_name = "ui/courses/id.html"
    success_message = _("Thanks for enrolling in this course")

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """Redirect to course detail page"""

        try:
            course = Course.objects.get(slug=self.kwargs["course"])
            return redirect(course.get_url(request))

        except Course.DoesNotExist:
            return redirect(reverse_lazy("ui:learn"))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """Check if user is enrolled in course to redirect to course page"""

        try:
            _enrollment = Enrollment.objects.get(
                owner=self.request.user,
                course__slug=self.kwargs["course"],
            )

            messages.info(request, _("You are enrolled in this course"))

            return redirect(reverse_lazy("ui:course", args=[self.kwargs["course"]]))

        except Enrollment.DoesNotExist:
            return super().post(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("ui:course", args=[self.kwargs["course"]])

    def form_valid(self, form: BaseForm) -> HttpResponse:
        """Add owner and course to enrollment"""

        enrollment = form.save(commit=False)
        enrollment.owner = self.request.user
        enrollment.course_id = self.kwargs["id"]

        return super().form_valid(form)


class CoursePostsView(CourseDetailView):
    """Course posts list"""

    template_name = "ui/learn/posts/list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add posts to context"""

        context = super().get_context_data(**kwargs)

        return {**context, "posts": Post.objects.live().child_of(context["course"])}


class ModuleDetailView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    generic.DetailView,
):
    """Module details"""

    model = Module
    slug_url_kwarg = "module"
    template_name = "ui/learn/content/module.html"


class PostDetailView(LoginRequiredMixin, mixins.CourseAccessMixin, generic.DetailView):
    """Post details"""

    model = Post
    slug_url_kwarg = "post"
    template_name = "ui/learn/posts/id.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add module to context"""

        context = super().get_context_data(**kwargs)

        return {
            **context,
            "course": context[self.slug_url_kwarg].get_parent(),
        }


class LessonDetailView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    generic.DetailView,
):
    """Lesson details"""

    model = Lesson
    slug_url_kwarg = "lesson"
    template_name = "ui/learn/content/lesson.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add module to context"""

        context = super().get_context_data(**kwargs)

        return {
            **context,
            "module": context[self.slug_url_kwarg].get_parent(),
        }


class ItemDetailView(LoginRequiredMixin, mixins.CourseAccessMixin, generic.DetailView):
    """Item details"""

    model = Item
    slug_url_kwarg = "item"
    template_name = "ui/learn/content/item.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add module to context"""

        context = super().get_context_data(**kwargs)

        return {
            **context,
            "lesson": context[self.slug_url_kwarg].get_parent(),
            "module": context[self.slug_url_kwarg].get_parent().get_parent(),
        }


class AssignmentDetailView(ItemDetailView):
    """Assignment details"""

    model = Assignment
    slug_url_kwarg = "assignment"
    template_name = "ui/learn/content/assignment.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add submission to context"""

        context = super().get_context_data(**kwargs)
        submissions = (
            context[self.slug_url_kwarg]
            .submissions.filter(owner=self.request.user)
            .order_by("-created_at")
        )

        return {
            **context,
            "submissions": submissions,
            "highest_grade": submissions.order_by("-grade").first(),
        }


class SubmissionCreateView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Submission create view"""

    model = Submission
    fields = []
    template_name = "ui/learn/content/assignment.html"
    success_message = _("Your assignment submitted successfully")

    def form_valid(self, form: BaseForm) -> HttpResponse:
        """Create submission"""

        submission = form.save(commit=False)
        submission.owner = self.request.user

        try:
            submission.assignment = Assignment.objects.get(
                slug=self.kwargs["assignment"]
            )
            submission.save()
            submission.answers.set(
                list(
                    flatten(
                        [
                            [int(i) for i in a[-1]]
                            for a in list(
                                filter(
                                    lambda i: i[0].startswith("question-"),
                                    self.request.POST.lists(),
                                )
                            )
                        ]
                    )
                )
            )
            submission.grade = submission.auto_grade()
            self.submission = submission

        except (Assignment.DoesNotExist, ValueError):
            return super().form_valid(form)

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            "ui:submission",
            args=[self.kwargs["course"], self.kwargs["assignment"], self.submission.id],
        )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add extra context"""

        context = super().get_context_data(**kwargs)
        assignment = context[self.slug_url_kwarg].assignment

        return {
            **context,
            "assignment": assignment,
            "lesson": assignment.get_parent(),
            "module": assignment.get_parent().get_parent(),
            "submissions": [context[self.slug_url_kwarg]],
        }


class SubmissionDetailView(
    LoginRequiredMixin,
    mixins.CourseAccessMixin,
    generic.DetailView,
):
    """Submission details"""

    model = Submission
    slug_url_kwarg = "submission"
    template_name = "ui/learn/content/submission.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add extra context"""

        context = super().get_context_data(**kwargs)
        assignment = context[self.slug_url_kwarg].assignment

        return {
            **context,
            "assignment": assignment,
            "lesson": assignment.get_parent(),
            "module": assignment.get_parent().get_parent(),
            "submissions": [context[self.slug_url_kwarg]],
        }
