""" Serializers for learn """


from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer


# Create your serializers here.
User = get_user_model()


class UserSerializer(HyperlinkedModelSerializer):
    """User serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = [
            "id",
            "url",
        ]
