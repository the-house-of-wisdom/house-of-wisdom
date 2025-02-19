"""Serializers for bayt_al_hikmah.lessons"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.lessons.models import Lesson


# Create your serializers here.
class LessonSerializer(ModelSerializer):
    """Lesson serializer"""

    class Meta:
        """Meta data"""

        model = Lesson
        fields = [
            "id",
            "url",
            "module",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
