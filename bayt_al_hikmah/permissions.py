"""Custom API access permissions"""

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from bayt_al_hikmah.enrollments.models import Enrollment


# Create your permissions here.
class DenyAll(BasePermission):
    """Deny all requests"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return False

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return False


class IsAccountOwner(BasePermission):
    """Check if the user is the owner of the account"""

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return request.user == obj


class IsInstructor(BasePermission):
    """Check if the user is an instructor"""

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return request.user.is_instructor


class IsOwner(BasePermission):
    """Check if the user is the owner of the obj"""

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return request.user.id == obj.owner_id


class IsEnrolledOrInstructor(BasePermission):
    """Check if the user is enrolled in course or is the instructor of the course"""

    def has_object_permission(self, request: Request, view: ModelViewSet, obj) -> bool:
        return (
            request.user.id == obj.owner_id
            or Enrollment.objects.filter(
                owner_id=request.user.id, course_id=view.kwargs["course_id"]
            ).exists()
        )
