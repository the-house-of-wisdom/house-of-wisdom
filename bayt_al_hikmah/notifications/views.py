"""API endpoints for bayt_al_hikmah.notifications"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.notifications.models import Notification
from bayt_al_hikmah.notifications.serializers import NotificationSerializer


# Create your views here.
class NotificationViewSet(ModelViewSet):
    """Create, view, update and delete Notifications"""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "type"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
