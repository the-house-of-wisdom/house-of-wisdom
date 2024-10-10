""" Permissions """

from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsAccountOwner(BasePermission):
    """Check if the current logged in user is the owner of the account"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsOwner(BasePermission):
    """Check if the current logged in user is the owner of the obj"""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user_id


class IsCourseOwner(BasePermission):
    """Check if the current logged in user is the owner of the course of the module or item"""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.course.user_id
