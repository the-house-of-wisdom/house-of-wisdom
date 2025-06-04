"""Serializers for how.notifications"""

from rest_framework.serializers import ModelSerializer

from how.notifications.models import Notification


# Create your serializers here.
class NotificationSerializer(ModelSerializer):
    """Notification serializer"""

    class Meta:
        """Meta data"""

        model = Notification
        read_only_fields = ["owner"]
        fields = [
            "id",
            "url",
            "owner",
            "content",
            "created_at",
            "updated_at",
        ]
