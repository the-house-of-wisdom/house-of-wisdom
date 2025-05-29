"""API endpoints for bayt_al_hikmah.categories"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.categories.serializers import CategorySerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin


# Create your views here.
class CategoryViewSet(ActionPermissionsMixin, ModelViewSet):
    """
    API endpoints for managing Categories.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for course categories.
    Categories help organize courses into thematic or subject-related groupings, making it easier for users
    to explore and filter available courses.

    ## Endpoints

    - **List Categories**
      `GET /api/categories`
      Retrieves a list of all course categories.

    - **Create Category**
      `POST /api/categories`
      Creates a new course category. Requires category details in the request body.

    - **Retrieve Category**
      `GET /api/categories/{id}`
      Retrieves detailed information for the category identified by `id`.

    - **Update Category**
      `PUT /api/categories/{id}`
      Fully updates an existing course category with the provided information.

    - **Partial Update Category**
      `PATCH /api/categories/{id}`
      Applies partial updates to the category.

    - **Delete Category**
      `DELETE /api/categories/{id}`
      Deletes the course category identified by `id`.

    ## Query Parameters

    - **search:**
      Filter categories by name or description (e.g., `?search=technology`).

    - **ordering:**
      Order categories by a specific field (e.g., `?ordering=name` for alphabetical order).

    ## Permissions

    - **Authenticated Users:**
      Can view the list of categories and retrieve category details.

    - **Admin/Staff Users:**
      Can create, update, or delete categories.

    ## Example API Requests

    **List Categories:**

    ```bash
    curl -X GET http://localhost:8000/api/categories \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Category:**

    ```bash
    curl -X POST http://localhost:8000/api/categories \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "name": "Technology",
                "description": "Courses related to technology, programming, and IT."
            }'
    ```

    **Retrieve Category Details:**

    ```bash
    curl -X GET http://localhost:8000/api/categories/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["name"]
    action_permissions = {
        "default": [IsAuthenticated, IsAdminUser],
        "list": permission_classes,
        "retrieve": permission_classes,
    }
