"""Views for bayt_al_hikmah.tags"""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bayt_al_hikmah.blog.models import Article
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.paths.models import Path
from bayt_al_hikmah.ui import mixins
from bayt_al_hikmah.ui.forms import UserCreateForm


# Create your views here.
class HomeView(generic.TemplateView):
    """Home page"""

    template_name = "ui/index.html"


# Auth views
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


# Articles
class ArticleListView(generic.ListView):
    """Article list"""

    paginate_by = 25
    ordering = "-created_at"
    template_name = "ui/articles/list.html"
    queryset = Article.objects.live().public()


class ArticleDetailView(generic.DetailView):
    """Article list"""

    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "ui/articles/id.html"
    queryset = Article.objects.live().public()


# Learning Paths
class PathListView(generic.ListView):
    """Learning path list"""

    model = Path
    paginate_by = 15
    template_name = "ui/paths/list.html"


class PathDetailView(generic.DetailView):
    """Learning path details"""

    model = Path
    slug_field = "slug"
    template_name = "ui/paths/id.html"


# Courses
class CourseListView(generic.ListView):
    """Course list"""

    model = Course
    paginate_by = 15
    template_name = "ui/courses/list.html"


class CourseDetailView(generic.DetailView):
    """Course details"""

    model = Course
    slug_field = "slug"
    template_name = "ui/courses/id.html"


class LearnCourseDetailView(mixins.InstructorOrStudentMixin, CourseDetailView):
    """Enrolled course detail view"""

    template_name = "ui/learn/list.html"
