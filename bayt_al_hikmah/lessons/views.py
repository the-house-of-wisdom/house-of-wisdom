""" API endpoints for bayt_al_hikmah.lessons """

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.lessons.serializers import LessonSerializer


# Create your views here.
class LessonViewSet(ModelViewSet):
    """Create, view, update and delete Lessons"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["module__course", "module"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
