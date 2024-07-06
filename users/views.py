""" API endpoints for learn.users """

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from learn.users.models import User
from learn.users.serializers import UserSerializer


# Create your views here.
class UserViewSet(ReadOnlyModelViewSet):
    """List and retrieve Users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["id", "title", "created_at", "updated_at"]
    filterset_fields = ["module", "title"]

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()
