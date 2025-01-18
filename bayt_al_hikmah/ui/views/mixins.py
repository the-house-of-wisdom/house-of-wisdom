""" View mixins """

from typing import Any
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your mixins here.
class ActiveUserMixin(UserPassesTestMixin):
    """Allow access to active users only"""

    def test_func(self) -> bool:
        return self.request.user.is_active


class AdminUserMixin(ActiveUserMixin):
    """Allow access to active admin users only"""

    def test_func(self) -> bool:
        return super().test_func() and self.request.user.is_staff


class InstructorUserMixin(ActiveUserMixin):
    """Allow access to active instructor users only"""

    def test_func(self) -> bool:
        return super().test_func() and self.request.user.is_instructor


class ExtraContextMixin:
    """Add title to default context"""

    extra_context: dict[str, Any]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Add title to context"""

        return {**super().get_context_data(**kwargs), **self.extra_context}


class OwnerMixin:
    """Add user automatically when creating"""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
