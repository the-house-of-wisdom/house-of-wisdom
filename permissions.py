""" Permissions """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Check if the current logged in user is the owner of the object"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
