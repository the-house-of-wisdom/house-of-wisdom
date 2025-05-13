"""API endpoints for bayt_al_hikmah.users"""

from djoser.views import UserViewSet as BaseUVS
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.permissions import IsAccountOwner


# Create your views here.
class UserViewSet(BaseUVS):
    """Create, view, update and delete Users"""

    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["username", "date_joined", "last_login"]
    filterset_fields = ["username", "is_instructor"]

    def get_permissions(self):
        """Add permissions for new actions"""

        match self.action:
            case "approve":
                self.permission_classes = [IsAuthenticated, IsAdminUser]

            case "join":
                self.permission_classes = [IsAuthenticated, IsAccountOwner]

        return super().get_permissions()

    @action(methods=["post"], detail=True)
    def approve(self, request: Request, id: int) -> Response:
        """Approve user request to be an instructor"""

        user = self.get_object()
        user.is_instructor = not user.is_instructor
        user.save()

        return Response(
            {
                "details": f"User '{user}' request {'approved' if user.is_instructor else 'rejected'}"
            },
            status=status.HTTP_200_OK,
        )

    @action(methods=["post"], detail=True)
    def join(self, request: Request, id: int) -> Response:
        """Join our platform and become an instructor"""

        message = ""
        user = self.get_object()

        if user.is_instructor is None:
            user.is_instructor = False
            user.save()
            message = "Your request to be an instructor is sent."

        elif user.is_instructor is False:
            message = "Your request is pending approval."

        else:
            message = "Your request is approved."

        return Response(
            {"details": message},
            status=status.HTTP_200_OK,
        )
