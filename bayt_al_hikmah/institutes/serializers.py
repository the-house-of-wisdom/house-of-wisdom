""" Serializers for bayt_al_hikmah.institutes """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.institutes.models import Institute


# Create your serializers here.
class InstituteSerializer(ModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Institute
        read_only_fields = ["user", "is_approved"]
        fields = [
            "id",
            "url",
            "user",
            "image",
            "name",
            "headline",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
