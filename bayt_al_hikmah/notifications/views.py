"""API endpoints for bayt_al_hikmah.notifications"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import UserFilterMixin
from bayt_al_hikmah.notifications.models import Notification
from bayt_al_hikmah.notifications.serializers import NotificationSerializer
from bayt_al_hikmah.permissions import IsOwner


# Create your views here.
class NotificationViewSet(UserFilterMixin, ReadOnlyModelViewSet):
    """Create, view, update and delete Notifications"""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "type"]
