"""View Mixins"""

from typing import Any, List
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.permissions import DenyAll, IsInstructor


# Create your mixins here.
# View Mixins
class OwnerMixin:
    """Add the owner of the object"""

    def perform_create(self, serializer):
        """Save the object with owner"""

        serializer.save(user=self.request.user)


class UserFilterMixin:
    """Filter queryset by user"""

    def get_queryset(self):
        """Perform the filter"""

        return super().get_queryset().filter(user_id=self.request.user.id)


class InstructorMixin:
    """Customize permissions"""

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsInstructor]

        return super().get_permissions()


class ActionPermDictMixin:
    """Allows you to set permissions for each action using a dict"""

    action_perm_dict = {"default": [IsAuthenticated]}

    def get_permissions(self) -> List[Any]:
        """Set permissions based on each action"""

        self.permission_classes = self.action_perm_dict.get(
            self.action, self.action_perm_dict["default"]
        )

        return super().get_permissions()
