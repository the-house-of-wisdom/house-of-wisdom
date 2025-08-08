"""Generic View Mixins for how.ui"""

from typing import Optional

from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import BaseModelForm
from django.http import HttpResponse

from how.apps.courses.models import Course
from how.apps.enrollments.models import Enrollment


# Create your mixins here.
class AdminUserMixin(UserPassesTestMixin):
    """Check if the user is an admin"""

    def test_func(self) -> Optional[bool]:
        return self.request.user.is_staff


class AccountOwnerMixin(UserPassesTestMixin):
    """Check if the user is owner of the account"""

    def test_func(self) -> Optional[bool]:
        return self.request.user == self.get_object()


class CourseAccessMixin(UserPassesTestMixin):
    """Check if the user is enrolled in the course or owner of the course"""

    def test_func(self) -> Optional[bool]:
        """Check fn"""

        try:
            course = Course.objects.get(slug=self.kwargs["course"])
            is_owner = self.request.user == course.owner
            is_enrolled = (
                Enrollment.objects.get(
                    course=course,
                    owner=self.request.user,
                )
                is not None
            )

            return is_owner or is_enrolled

        except (Course.DoesNotExist, Enrollment.DoesNotExist):
            return False


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
