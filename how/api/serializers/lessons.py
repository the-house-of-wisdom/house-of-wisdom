"""Serializers for how.apps.lessons"""

from rest_framework.serializers import ModelSerializer

from how.apps.lessons.models import Lesson


# Create your serializers here.
class LessonSerializer(ModelSerializer):
    """Lesson serializer"""

    class Meta:
        """Meta data"""

        model = Lesson
        fields = [
            "id",
            "url",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
