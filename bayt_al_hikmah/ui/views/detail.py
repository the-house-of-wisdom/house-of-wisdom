""" Detail views """

from django.views.generic import DetailView

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.departments.models import Department
from bayt_al_hikmah.faculties.models import Faculty
from bayt_al_hikmah.specializations.models import Specialization
from bayt_al_hikmah.tags.models import Tag
from bayt_al_hikmah.ui.views.mixins import AdminUserMixin, ExtraContextMixin


# Create your detail views here.
class ModelDetailView(ExtraContextMixin, DetailView):
    """View details of a Model"""

    extra_context = {"title": "Model details"}
    pk_url_kwarg = "id"


class CategoryDetailView(AdminUserMixin, ModelDetailView):
    """View details of a Category"""

    model = Category
    extra_context = {"title": "Category details"}
    template_name = "bah_ui/detail/category.html"


class CourseDetailView(ModelDetailView):
    """View details of a Course"""

    model = Course
    extra_context = {"title": "Course details"}
    template_name = "bah_ui/detail/course.html"


class DepartmentDetailView(ModelDetailView):
    """View details of a Department"""

    model = Department
    extra_context = {"title": "Department details"}
    template_name = "bah_ui/detail/department.html"


class FacultyDetailView(ModelDetailView):
    """View details of a Faculty"""

    model = Faculty
    extra_context = {"title": "Faculty details"}
    template_name = "bah_ui/detail/faculty.html"


class SpecializationDetailView(ModelDetailView):
    """View details of a Specialization"""

    model = Specialization
    extra_context = {"title": "Specialization details"}
    template_name = "bah_ui/detail/specialization.html"


class TagDetailView(AdminUserMixin, ModelDetailView):
    """View details of a Tag"""

    model = Tag
    extra_context = {"title": "Tag details"}
    template_name = "bah_ui/detail/tag.html"
