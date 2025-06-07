"""Generic View Mixins for how.ui"""

from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import BaseModelForm
from django.http import HttpResponse

from how.enrollments.models import Enrollment


# Create your mixins here.
class AdminUserMixin(UserPassesTestMixin):
    """Check if the user is an admin"""

    def test_func(self) -> Optional[bool]:
        return self.request.user.is_staff


class AccountOwnerMixin(UserPassesTestMixin):
    """Check if the user is owner of the account"""

    def test_func(self) -> Optional[bool]:
        return self.request.user == self.get_object()


class InstructorMixin(UserPassesTestMixin):
    """Check if the user is an instructor"""

    def test_func(self) -> Optional[bool]:
        return self.request.user.is_instructor


class InstructorOrStudentMixin(InstructorMixin):
    """Check if the user is an instructor"""

    def test_func(self) -> Optional[bool]:
        return (
            super().test_func()
            or Enrollment.objects.filter(
                owner_id=self.request.user.id, course_id=self.kwargs["course_id"]
            ).exists()
        )


class OwnerMixin:
    """Adds the owner automatically"""

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Add the owner of the object automatically"""

        obj = form.save(commit=False)
        obj.owner_id = self.request.user.id

        return super().form_valid(form)
