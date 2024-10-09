""" Serializers for bayt_al_hikmah.users """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.users.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = [
            "id",
            "url",
            "image",
            "username",
            "first_name",
            "last_name",
        ]
