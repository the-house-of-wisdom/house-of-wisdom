"""API endpoints for how.notifications"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from how.mixins.views import UserFilterMixin
from how.notifications.models import Notification
from how.notifications.serializers import NotificationSerializer
from how.permissions import IsOwner


# Create your views here.
class NotificationViewSet(UserFilterMixin, ReadOnlyModelViewSet):
    """Create, view, update and delete Notifications"""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner", "type"]
