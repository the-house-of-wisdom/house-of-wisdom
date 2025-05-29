"""API endpoints for bayt_al_hikmah.reviews"""

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.reviews.models import Review
from bayt_al_hikmah.reviews.serializers import ReviewSerializer
from bayt_al_hikmah.permissions import DenyAll, IsEnrolledOrInstructor, IsOwner


# Create your views here.
class BaseReviewVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["comment"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "course", "rating", "sentiment"]
    action_permissions = {
        "default": [IsAuthenticated, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
    }


class ReviewViewSet(BaseReviewVS):
    """
    API endpoints for managing Reviews.

    ## Overview

    API endpoints provide full RUD (Retrieve, Update, Delete) functionality for course reviews.
    Users can rate and provide feedback on courses, and these reviews help inform both instructors and prospective students.
    Reviews can also be moderated by administrators.

    ## Endpoints

    - **List Reviews**
      `GET /api/reviews`
      Retrieves a list of all course reviews.

    - **Retrieve Review**
      `GET /api/reviews/{id}`
      Retrieves detailed information for the review identified by `id`.

    - **Update Review**
      `PUT /api/reviews/{id}`
      Fully updates an existing review with the provided data.

    - **Partial Update Review**
      `PATCH /api/reviews/{id}`
      Applies partial updates to the review.

    - **Delete Review**
      `DELETE /api/reviews/{id}`
      Deletes the review identified by `id`.

    ## Query Parameters

    - **user:**
      Filter reviews by reviewer (e.g., `?user=1`).

    - **course:**
      Filter reviews by course (e.g., `?course=1`).

    - **rating:**
      Filter reviews by rating (e.g., `?rating=5`).

    - **sentiment:**
      Filter reviews by sentiment (e.g., `?sentiment=0`).

    - **search:**
      Filter reviews by keywords found in the comment (e.g., `?search=excellent`).

    - **ordering:**
      Order reviews by a specific field (e.g., `?ordering=-created_at` for newest reviews first or `?ordering=rating`).

    ## Permissions

    - **Authenticated Users:**
      Can create reviews and view their own review history. Users can update or delete only their own reviews.

    - **Instructors/Admins:**
      Can view, moderate, and remove any reviews. They may also have the ability to flag inappropriate content.

    ## Example API Requests

    **List Course Reviews:**

    ```bash
    curl -X GET http://localhost:8000/api/reviews \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Retrieve a Course Review:**

    ```bash
    curl -X GET http://localhost:8000/api/reviews/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {**BaseReviewVS.action_permissions, "create": [DenyAll]}

    def get_queryset(self):
        """
        Filter queryset by user to allow users to view their reviews only and
        allow instructors to view reviews of their courses.
        """

        return (
            super()
            .get_queryset()
            .filter(
                Q(user_id=self.request.user.id)
                | Q(course__user_id=self.request.user.id)
            )
        )


class CourseReviews(BaseReviewVS):
    """
    API endpoints for managing Course Reviews.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for course reviews.
    Users can rate and provide feedback on courses, and these reviews help inform both instructors and prospective students.
    Reviews can also be moderated by administrators.

    ## Endpoints

    - **List Reviews**
      `GET /api/courses/{courseId}/reviews`
      Retrieves a list of all course reviews.

    - **Create Review**
      `POST /api/courses/{courseId}/reviews`
      Creates a new course review. Requires review details in the request body.

    - **Retrieve Review**
      `GET /api/courses/{courseId}/reviews/{id}`
      Retrieves detailed information for the review identified by `id`.

    - **Update Review**
      `PUT /api/courses/{courseId}/reviews/{id}`
      Fully updates an existing review with the provided data.

    - **Partial Update Review**
      `PATCH /api/courses/{courseId}/reviews/{id}`
      Applies partial updates to the review.

    - **Delete Review**
      `DELETE /api/courses/{courseId}/reviews/{id}`
      Deletes the review identified by `id`.

    ## Query Parameters

    - **user:**
      Filter reviews by reviewer (e.g., `?user=1`).

    - **rating:**
      Filter reviews by rating (e.g., `?rating=5`).

    - **sentiment:**
      Filter reviews by sentiment (e.g., `?sentiment=0`).

    - **search:**
      Filter reviews by keywords found in the comment (e.g., `?search=excellent`).

    - **ordering:**
      Order reviews by a specific field (e.g., `?ordering=-created_at` for newest reviews first or `?ordering=rating`).

    ## Permissions

    - **Authenticated Users:**
      Can create reviews and view their own review history. Users can update or delete only their own reviews.

    - **Instructors/Admins:**
      Can view, moderate, and remove any reviews. They may also have the ability to flag inappropriate content.

    ## Example API Requests

    **List Course Reviews:**

    ```bash
    curl -X GET http://localhost:8000/api/courses/1/reviews \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Course Review:**

    ```bash
    curl -X POST http://localhost:8000/api/courses/1/reviews \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "rating": 5,
                "comment": "Outstanding Course! This course was extremely informative and well-structured."
            }'
    ```

    **Retrieve a Course Review:**

    ```bash
    curl -X GET http://localhost:8000/api/courses/1/reviews/1
    ```
    """

    action_permissions = {
        **BaseReviewVS.action_permissions,
        "create": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add course to review automatically"""

        serializer.save(
            user_id=self.request.user.id, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
