"""Update views"""

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

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


# Create your update views here.
class ModelUpdateView(ExtraContextMixin, LoginRequiredMixin, UpdateView):
    """Update a Model"""

    pk_url_kwarg = "id"
    extra_context = {"title": "Update Model"}
    template_name = "ui/shared/form.html"


class CategoryUpdateView(AdminUserMixin, ModelUpdateView):
    """Update a Category"""

    model = Category
    extra_context = {"title": "Update Category"}
    fields = ["name", "description"]
    success_url = reverse_lazy("ui:categories")


class CourseUpdateView(ModelUpdateView):
    """Update a Course"""

    model = Course
    extra_context = {"title": "Update Course"}
    fields = [
        "category",
        "department",
        "tags",
        "image",
        "name",
        "headline",
        "description",
    ]
    success_url = reverse_lazy("ui:courses")


class DepartmentUpdateView(AdminUserMixin, ModelUpdateView):
    """Update a Department"""

    model = Department
    extra_context = {"title": "Update Department"}
    fields = ["faculty", "image", "name", "headline", "description"]
    success_url = reverse_lazy("ui:departments")


class FacultyUpdateView(AdminUserMixin, ModelUpdateView):
    """Update a Faculty"""

    model = Faculty
    extra_context = {"title": "Update Faculty"}
    fields = ["image", "name", "headline", "description"]
    success_url = reverse_lazy("ui:faculties")


class ItemUpdateView(ModelUpdateView):
    """Update an Item"""

    model = Item
    fields = ["lesson", "title", "description", "content", "type"]
    success_url = reverse_lazy("ui:items")


class ModuleUpdateView(ModelUpdateView):
    """Update a Module"""

    model = Module
    extra_context = {"title": "Update Module"}
    fields = ["course", "title", "description"]
    success_url = reverse_lazy("ui:modules")


class ReviewUpdateView(ModelUpdateView):
    """Update a Review"""

    model = Review
    extra_context = {"title": "Update Review"}
    fields = ["rating", "comment"]
    success_url = reverse_lazy("ui:reviews")


class LessonUpdateView(ModelUpdateView):
    """Update a Lesson"""

    model = Lesson
    extra_context = {"title": "Update Lesson"}
    fields = ["module", "title", "description"]
    success_url = reverse_lazy("ui:lessons")


class SpecializationUpdateView(ModelUpdateView):
    """Update a Specialization"""

    model = Specialization
    extra_context = {"title": "Update Specialization"}
    fields = [
        "category",
        "department",
        "tags",
        "image",
        "name",
        "headline",
        "description",
    ]
    success_url = reverse_lazy("ui:specializations")


class TagUpdateView(AdminUserMixin, ModelUpdateView):
    """Update a Tag"""

    model = Tag
    extra_context = {"title": "Update Tag"}
    fields = ["name", "description"]
    success_url = reverse_lazy("ui:tags")
