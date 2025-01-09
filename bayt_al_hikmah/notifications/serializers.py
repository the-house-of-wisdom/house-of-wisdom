""" Serializers for bayt_al_hikmah.notifications """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.notifications.models import Notification


# Create your serializers here.
class NotificationSerializer(ModelSerializer):
    """Notification serializer"""

    class Meta:
        """Meta data"""

        model = Notification
        fields = [
            "id",
            "url",
            "user",
            "content",
            "created_at",
            "updated_at",
        ]
