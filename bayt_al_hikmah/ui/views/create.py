""" Create views """

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.departments.models import Department
from bayt_al_hikmah.faculties.models import Faculty
from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.reviews.models import Review
from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.specializations.models import Specialization
from bayt_al_hikmah.tags.models import Tag
from bayt_al_hikmah.ui.views.mixins import AdminUserMixin, ExtraContextMixin


# Create your create views here.
class ModelCreateView(ExtraContextMixin, LoginRequiredMixin, CreateView):
    """Create a Model"""

    extra_context = {"title ": "New Model"}
    template_name = "bah_ui/shared/form.html"


class CategoryCreateView(AdminUserMixin, ModelCreateView):
    """Create a Category"""

    model = Category
    extra_context = {"title ": "New Category"}
    fields = ["name", "description"]
    success_url = reverse_lazy("bah-ui:categories")


class CourseCreateView(ModelCreateView):
    """Create a Course"""

    model = Course
    extra_context = {"title ": "New Course"}
    fields = [
        "category",
        "department",
        "tags",
        "image",
        "name",
        "headline",
        "description",
    ]
    success_url = reverse_lazy("bah-ui:courses")


class DepartmentCreateView(AdminUserMixin, ModelCreateView):
    """Create a Department"""

    model = Department
    extra_context = {"title ": "New Department"}
    fields = ["faculty", "image", "name", "headline", "description"]
    success_url = reverse_lazy("bah-ui:departments")


class FacultyCreateView(AdminUserMixin, ModelCreateView):
    """Create a Faculty"""

    model = Faculty
    extra_context = {"title ": "New Faculty"}
    fields = ["image", "name", "headline", "description"]
    success_url = reverse_lazy("bah-ui:faculties")


class ItemCreateView(ModelCreateView):
    """Create an Item"""

    model = Item
    fields = ["lesson", "title", "description", "content", "type"]
    success_url = reverse_lazy("bah-ui:items")


class ModuleCreateView(ModelCreateView):
    """Create a Module"""

    model = Module
    extra_context = {"title ": "New Module"}
    fields = ["course", "title", "description"]
    success_url = reverse_lazy("bah-ui:modules")


class ReviewCreateView(ModelCreateView):
    """Create a Review"""

    model = Review
    extra_context = {"title ": "New Review"}
    fields = ["rating", "comment"]
    success_url = reverse_lazy("bah-ui:reviews")


class LessonCreateView(ModelCreateView):
    """Create a Lesson"""

    model = Lesson
    extra_context = {"title ": "New Lesson"}
    fields = ["module", "title", "description"]
    success_url = reverse_lazy("bah-ui:lessons")


class SpecializationCreateView(ModelCreateView):
    """Create a Specialization"""

    model = Specialization
    extra_context = {"title ": "New Specialization"}
    fields = [
        "category",
        "department",
        "tags",
        "image",
        "name",
        "headline",
        "description",
    ]
    success_url = reverse_lazy("bah-ui:specializations")


class TagCreateView(AdminUserMixin, ModelCreateView):
    """Create a Tag"""

    model = Tag
    extra_context = {"title ": "New Tag"}
    fields = ["name", "description"]
    success_url = reverse_lazy("bah-ui:tags")
