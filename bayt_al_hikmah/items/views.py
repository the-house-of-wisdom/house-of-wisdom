"""API endpoints for bayt_al_hikmah.items"""

from typing import Any, List
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.items.serializers import ItemSerializer
from bayt_al_hikmah.permissions import IsInstructor


# Create your views here.
class ItemViewSet(ModelViewSet):
    """Create, view, update and delete Module Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson", "type"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsInstructor]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(lesson__module__course__user_id=self.request.user.pk)
                | Q(lesson__module__course__students=self.request.user)
            )
        )

    @action(methods=["post"], detail=True)
    def mark(self, request: Request, pk: int) -> Response:
        """Mark a course lesson item as un/completed"""

        is_completed = False
        item = self.get_object()

        if not request.user.items.contains(item):
            is_completed = True
            request.user.items.add(item)

        else:
            request.user.items.remove(item)

        item.save()

        return Response(
            {
                "details": f"Item '{item}' marked as {'completed' if is_completed else 'uncompleted'}"
            },
            status=status.HTTP_200_OK,
        )


class LessonItemsViewSet(ItemViewSet):
    """Create, view, update and delete Lesson Items"""

    def perform_create(self, serializer):
        """Create an item with lesson set automatically"""

        serializer.save(lesson_id=self.kwargs["lesson_id"])

    def get_queryset(self):
        """Filter queryset by lesson"""

        return super().get_queryset().filter(lesson_id=self.kwargs["lesson_id"])
