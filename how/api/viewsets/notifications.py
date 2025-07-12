"""API endpoints for how.apps.notifications"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from how.api.mixins import UserFilterMixin
from how.api.permissions import IsOwner
from how.api.serializers.notifications import NotificationSerializer
from how.apps.notifications.models import Notification


# Create your views here.
class NotificationViewSet(UserFilterMixin, ReadOnlyModelViewSet):
    """Create, view, update and delete Notifications"""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner", "type"]
