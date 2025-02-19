"""Permissions"""

from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsActive(BasePermission):
    """Check if the user's account is activated"""

    def has_permission(self, request, view):
        return request.user.is_instructor


class IsAccountOwner(BasePermission):
    """Check if the user is the owner of the account"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsOwner(BasePermission):
    """Check if the user is the owner of the obj"""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user_id


class IsInstructor(BasePermission):
    """Check if the user is an instructor"""

    def has_permission(self, request, view):
        return request.user.is_instructor
