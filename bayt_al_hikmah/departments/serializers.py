"""Serializers for bayt_al_hikmah.departments"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.departments.models import Department


# Create your serializers here.
class DepartmentSerializer(ModelSerializer):
    """Department serializer"""

    class Meta:
        """Meta data"""

        model = Department
        fields = [
            "id",
            "url",
            "faculty",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
        ]
