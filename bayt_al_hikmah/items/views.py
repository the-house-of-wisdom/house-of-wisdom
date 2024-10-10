""" API endpoints for bayt_al_hikmah.items """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.items.serializers import ItemSerializer
from bayt_al_hikmah.permissions import IsCourseOwner


# Create your views here.
class ItemViewSet(ModelViewSet):
    """Create, view, update and delete Module Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["title", "created_at", "updated_at"]
    filterset_fields = ["course", "module", "type"]

    def get_permissions(self):
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsCourseOwner]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(course__user=self.request.user)


class ModuleItemsViewSet(ItemViewSet):
    """Items of a module"""

    def get_queryset(self):
        """Filter queryset by course"""

        return (
            super()
            .get_queryset()
            .filter(
                course_id=self.kwargs["course_id"],
                module_id=self.kwargs["module_id"],
            )
        )

    def perform_create(self, serializer):
        """Add module to item"""

        serializer.save(
            course_id=self.kwargs["course_id"],
            module_id=self.kwargs["module_id"],
        )
