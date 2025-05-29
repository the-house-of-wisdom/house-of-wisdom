"""API endpoints for bayt_al_hikmah.tags"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.tags.models import Tag
from bayt_al_hikmah.tags.serializers import TagSerializer


# Create your views here.
class TagViewSet(ActionPermissionsMixin, ModelViewSet):
    """
    API endpoints for managing Tags applied to courses.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for tags.
    Tags serve as labels or keywords that help categorize and filter courses by topics, technologies,
    or any custom taxonomy. Using tags, users can easily search for courses that match a particular interest or subject.

    ## Endpoints

    - **List Tags**
      `GET /api/tags`
      Retrieves a list of all available tags.

    - **Create Tag**
      `POST /api/tags`
      Creates a new tag. Requires tag details in the request body.

    - **Retrieve Tag**
      `GET /api/tags/{id}`
      Retrieves detailed information for the tag identified by `id`.

    - **Update Tag**
      `PUT /api/tags/{id}`
      Fully updates an existing tag with new details.

    - **Partial Update Tag**
      `PATCH /api/tags/{id}`
      Applies partial updates to the tag.

    - **Delete Tag**
      `DELETE /api/tags/{id}`
      Deletes the tag identified by `id`.

    ## Query Parameters

    - **name:**
      Filter tags by name (e.g., `?name=python`).

    - **search:**
      Filter tags by name or description (e.g., `?search=python`).

    - **ordering:**
      Order tags by a specific field (e.g., `?ordering=name` to sort alphabetically).

    ## Permissions

    - **Authenticated Users:**
      Can view tags and retrieve tag details.

    - **Admin/Staff Users:**
      Can create, update, and delete tags.

    ## Example API Requests

    **List Tags:**

    ```bash
    curl -X GET http://localhost:8000/api/tags \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Tag:**

    ```bash
    curl -X POST http://localhost:8000/api/tags \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "name": "Python",
                "description": "Courses related to Python programming."
            }'
    ```

    **Retrieve a Single Tag:**

    ```bash
    curl -X GET http://localhost:8000/api/tags/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Update a Tag:**

    ```bash
    curl -X PUT http://localhost:8000/api/tags/1 \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "name": "Advanced Python",
                "description": "Advanced topics in Python programming."
            }'
    ```
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["tag", "created_at", "updated_at"]
    filterset_fields = ["name"]
    action_permissions = {
        "default": [IsAuthenticated, IsAdminUser],
        "list": permission_classes,
        "retrieve": permission_classes,
    }
