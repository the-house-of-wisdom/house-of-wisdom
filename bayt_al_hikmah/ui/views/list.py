""" List views """

from django.views.generic import ListView

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.departments.models import Department
from bayt_al_hikmah.faculties.models import Faculty
from bayt_al_hikmah.specializations.models import Specialization
from bayt_al_hikmah.tags.models import Tag
from bayt_al_hikmah.ui.views.mixins import AdminUserMixin, ExtraContextMixin


# Create your list views here.
class ModelListView(ExtraContextMixin, ListView):
    """View a list of Models"""

    extra_context = {"title": "Models"}


class CategoryListView(AdminUserMixin, ModelListView):
    """View a list of Categories"""

    model = Category
    extra_context = {"title": "Categories"}
    template_name = "bah_ui/list/category.html"


class CourseListView(ModelListView):
    """View a list of Courses"""

    model = Course
    extra_context = {"title": "Courses"}
    template_name = "bah_ui/list/course.html"


class DepartmentListView(ModelListView):
    """View a list of Departments"""

    model = Department
    extra_context = {"title": "Departments"}
    template_name = "bah_ui/list/department.html"


class FacultyListView(ModelListView):
    """View a list of Faculties"""

    model = Faculty
    extra_context = {"title": "Faculties"}
    template_name = "bah_ui/list/faculty.html"


class SpecializationListView(ModelListView):
    """View a list of Specializations"""

    model = Specialization
    extra_context = {"title": "Specializations"}
    template_name = "bah_ui/list/specialization.html"


class TagListView(AdminUserMixin, ModelListView):
    """View a list of Tags"""

    model = Tag
    extra_context = {"title": "Tags"}
    template_name = "bah_ui/list/tag.html"
