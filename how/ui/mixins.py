"""Generic View Mixins for how.ui"""

from typing import Optional

from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import BaseModelForm
from django.http import HttpResponse


# Create your mixins here.
class AdminUserMixin(UserPassesTestMixin):
    """Check if the user is an admin"""

    def test_func(self) -> Optional[bool]:
        return self.request.user.is_staff


class AccountOwnerMixin(UserPassesTestMixin):
    """Check if the user is owner of the account"""

    def test_func(self) -> Optional[bool]:
        return self.request.user == self.get_object()


class StudentMixin(UserPassesTestMixin):
    """Check if the user is enrolled in the course or owner of the course"""

    def get_course(self):
        """Return the course"""

        return self.get_object()

    def test_func(self) -> Optional[bool]:
        """Check fn"""

        course = self.get_course()

        return self.request.user == course.owner or course.students.contains(
            self.request.user
        )


class ModuleStudentMixin(StudentMixin):
    """Check if the user is enrolled in the course or owner of the course"""

    def get_course(self):
        """Return the course"""

        return self.get_object().get_parent().specific


class LessonStudentMixin(StudentMixin):
    """Check if the user is enrolled in the course or owner of the course"""

    def get_course(self):
        """Return the course"""

        return self.get_object().get_parent().get_parent().specific


class ItemStudentMixin(StudentMixin):
    """Check if the user is enrolled in the course or owner of the course"""

    def get_course(self):
        """Return the course"""

        return self.get_object().get_parent().get_parent().get_parent().specific


class SubmissionStudentMixin(StudentMixin):
    """Check if the user is enrolled in the course or owner of the course"""

    def get_course(self):
        """Return the course"""

        return (
            self.get_object().assignment.get_parent().get_parent().get_parent().specific
        )


class ObjectOwnerMixin:
    """Adds the owner automatically"""

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Add the owner of the object automatically"""

        obj = form.save(commit=False)
        obj.owner_id = self.request.user.id

        return super().form_valid(form)


class OwnerFilterMixin:
    """Filters queryset by owner"""

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
