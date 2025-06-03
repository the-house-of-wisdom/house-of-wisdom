"""API endpoints for bayt_al_hikmah.posts"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin, UserFilterMixin
from bayt_al_hikmah.posts.models import Post
from bayt_al_hikmah.posts.serializers import PostSerializer
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsEnrolledOrInstructor,
    IsInstructor,
    IsOwner,
)


# Create your views here.
class BasePostVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Post.objects.live()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner", "type"]
    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
    }


class PostViewSet(UserFilterMixin, BasePostVS):
    """
    API endpoints for managing Posts.

    ## Overview

    API endpoints provides full RUD (Retrieve, Update, Delete) functionality for course posts.
    These posts are designed to allow instructors and course administrators to:

    - Publish announcements, updates, or important notices.
    - Share additional course-related information and supplementary content.
    - Engage students by keeping them informed about course changes, deadlines, or events.

    Only authorized instructors or course admins can create, update, or delete posts, while enrolled students have read-only access.

    ## Endpoints

    - **List Course Posts**
        `GET /api/posts`
        Retrieves a list of all course posts. Supports filtering by course and/or keywords in the post title or content.

    - **Retrieve Course Post**
        `GET /api/posts/{id}`
        Retrieves detailed information for a specific course post identified by `id`.

    - **Update Course Post**
        `PUT /api/posts/{id}`
        Fully updates an existing course post with new details provided in the request body.

    - **Partial Update Course Post**
        `PATCH /api/posts/{id}`
        Applies partial updates to an existing post (e.g., updating the post content or status).

    - **Delete Course Post**
        `DELETE /api/posts/{id}`
        Deletes the course post identified by `id`.

    ## Query Parameters

    - **type:**
        Filter posts by type (e.g., `?type=1`).

    - **course:**
        Filter posts by course (e.g., `?course=1`).

    - **search:**
        Filter posts by title or content keywords (e.g., `?search=update`).

    - **ordering:**
        Order posts by a specific field (e.g., `?ordering=-created_at` to list the most recent posts first).

    ## Permissions

    - **Instructors/Admins:**
        Can create, update, and delete posts for courses they manage.

    ## Example API Requests

    **List Course Posts:**

    ```bash
    curl -X GET /api/posts \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Partial Update (e.g., Update Content):**

    ```bash
    curl -X PATCH /api/posts/5 \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "content": "Updated content: Please note that the webinar..."
            }'
    ```

    **Delete a Course Post:**

    ```bash
    curl -X DELETE /api/posts/5 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ## Additional Notes

    Course posts serve as a central communication tool within the platform, ensuring that students are constantly
    updated with the latest course information. By using the CoursePostViewSet, instructors can create an engaging,
    informative, and dynamic course environment.
    """

    action_permissions = {**BasePostVS.action_permissions, "create": [DenyAll]}


class CoursePosts(BasePostVS):
    """
    API endpoints for managing Course Posts.

    ## Overview

    API endpoints provides full CRUD (Create, Retrieve, Update, Delete) functionality for course posts.
    These posts are designed to allow instructors and course administrators to:

    - Publish announcements, updates, or important notices.
    - Share additional course-related information and supplementary content.
    - Engage students by keeping them informed about course changes, deadlines, or events.

    Only authorized instructors or course admins can create, update, or delete posts, while enrolled students have read-only access.

    ## Endpoints

    - **List Course Posts**
        `GET /api/courses/{courseId}/posts`
        Retrieves a list of all course posts. Supports filtering by course and/or keywords in the post title or content.

    - **Create Course Post**
        `POST /api/courses/{courseId}/posts`
        Creates a new course post. Requires instructor credentials and post details in the request body.

    - **Retrieve Course Post**
        `GET /api/courses/{courseId}/posts/{id}`
        Retrieves detailed information for a specific course post identified by `id`.

    - **Update Course Post**
        `PUT /api/courses/{courseId}/posts/{id}`
        Fully updates an existing course post with new details provided in the request body.

    - **Partial Update Course Post**
        `PATCH /api/courses/{courseId}/posts/{id}`
        Applies partial updates to an existing post (e.g., updating the post content or status).

    - **Delete Course Post**
        `DELETE /api/courses/{courseId}/posts/{id}`
        Deletes the course post identified by `id`.

    ## Query Parameters

    - **type:**
        Filter posts by type (e.g., `?type=1`).

    - **search:**
        Filter posts by title or content keywords (e.g., `?search=update`).

    - **ordering:**
        Order posts by a specific field (e.g., `?ordering=-created_at` to list the most recent posts first).

    ## Permissions

    - **Students:**
        Can view course posts related to the courses in which they are enrolled.

    - **Instructors/Admins:**
        Can create, update, and delete posts for courses they manage.

    ## Example API Requests

    **List Course Posts:**

    ```bash
    curl -X GET /api/courses/1/posts
    ```

    **Create a Course Post:**

    ```bash
    curl -X POST /api/courses/1/posts \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "type": 0,
                "title": "Welcome to the Course!",
                "content": "We are excited to start..."
            }'
    ```

    **Partial Update (e.g., Update Content):**

    ```bash
    curl -X PATCH /api/posts/5 \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "content": "Please note that the webinar..."
            }'
    ```

    **Delete a Course Post:**

    ```bash
    curl -X DELETE /api/posts/5 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ## Additional Notes

    Course posts serve as a central communication tool within the platform, ensuring that students are constantly
    updated with the latest course information. By using the CoursePostViewSet, instructors can create an engaging,
    informative, and dynamic course environment.
    """

    action_permissions = {
        **BasePostVS.action_permissions,
        "default": [IsAuthenticated, IsInstructor],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add course to post automatically"""

        Course.objects.get(pk=self.kwargs["assignment_id"]).add_child(
            instance=Post(**serializer.validated_data, owner_id=self.request.user.pk)
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return (
            super()
            .get_queryset()
            .child_of(Course.objects.get(course_id=self.kwargs["course_id"]))
        )
