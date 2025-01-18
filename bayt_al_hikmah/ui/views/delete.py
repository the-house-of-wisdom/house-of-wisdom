""" Delete views """

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.departments.models import Department
from bayt_al_hikmah.enrollments.models import Enrollment
from bayt_al_hikmah.faculties.models import Faculty
from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.notifications.models import Notification
from bayt_al_hikmah.reviews.models import Review
from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.specializations.models import Specialization
from bayt_al_hikmah.tags.models import Tag
from bayt_al_hikmah.ui.views.mixins import AdminUserMixin, ExtraContextMixin


# Create your delete views here.
class ModelDeleteView(ExtraContextMixin, LoginRequiredMixin, DeleteView):
    """Delete a Model"""

    pk_url_kwarg = "id"
    extra_context = {"title": "Delete Model"}
    template_name = "bah_ui/shared/from.html"


class CategoryDeleteView(AdminUserMixin, ModelDeleteView):
    """Delete a Category"""

    model = Category
    extra_context = {"title": "Delete Category"}
    success_url = reverse_lazy("bah-ui:categories")


class CourseDeleteView(ModelDeleteView):
    """Delete a Course"""

    model = Course
    extra_context = {"title": "Delete Course"}
    success_url = reverse_lazy("bah-ui:courses")


class DepartmentDeleteView(AdminUserMixin, ModelDeleteView):
    """Delete a Department"""

    model = Department
    extra_context = {"title": "Delete Department"}
    success_url = reverse_lazy("bah-ui:departments")


class EnrollmentDeleteView(ModelDeleteView):
    """Delete a Enrollment"""

    model = Enrollment
    extra_context = {"title": "Delete Enrollment"}
    success_url = reverse_lazy("bah-ui:enrollments")


class FacultyDeleteView(AdminUserMixin, ModelDeleteView):
    """Delete a Faculty"""

    model = Faculty
    extra_context = {"title": "Delete Faculty"}
    success_url = reverse_lazy("bah-ui:faculties")


class ItemDeleteView(ModelDeleteView):
    """Delete an Item"""

    model = Item
    success_url = reverse_lazy("bah-ui:items")


class ModuleDeleteView(ModelDeleteView):
    """Delete a Module"""

    model = Module
    extra_context = {"title": "Delete Module"}
    success_url = reverse_lazy("bah-ui:modules")


class NotificationDeleteView(ModelDeleteView):
    """Delete a Notification"""

    model = Notification
    extra_context = {"title": "Delete Notification"}
    success_url = reverse_lazy("bah-ui:notifications")


class ReviewDeleteView(ModelDeleteView):
    """Delete a Review"""

    model = Review
    extra_context = {"title": "Delete Review"}
    success_url = reverse_lazy("bah-ui:reviews")


class LessonDeleteView(ModelDeleteView):
    """Delete a Lesson"""

    model = Lesson
    extra_context = {"title": "Delete Lesson"}
    success_url = reverse_lazy("bah-ui:lessons")


class SpecializationDeleteView(ModelDeleteView):
    """Delete a Specialization"""

    model = Specialization
    extra_context = {"title": "Delete Specialization"}
    success_url = reverse_lazy("bah-ui:specializations")


class TagDeleteView(AdminUserMixin, ModelDeleteView):
    """Delete a Tag"""

    model = Tag
    extra_context = {"title": "Delete Tag"}
    success_url = reverse_lazy("bah-ui:tags")
