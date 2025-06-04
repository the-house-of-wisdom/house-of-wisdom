"""Documented APIRootViews"""

from rest_framework.routers import APIRootView


# Create your views here.
class HouseOfWisdomAPI(APIRootView):
    """
    ## Overview

    Welcome to the API of House Of Wisdom, a cutting-edge, open source platform that leverages
    **advanced AI technologies** to deliver a personalized and adaptive learning management system (LMS).
    This project integrates a wide variety of features such as user management, course creation, intelligent tutoring,
    adaptive assessments, and more—all designed to revolutionize online education.

    ## Project Information

    **House Of Wisdom** focuses on:

    - **Personalized Learning:** Adaptive courses that tailor content according to individual learner progress and preferences.
    - **AI-powered Assistance:** Virtual tutors and content generation powered by state-of-the-art language models.
    - **Robust Educational Ecosystem:** Comprehensive modules for courses, lessons, assignments, enrollment, reviews,
      learning paths, course categories, tags, and more.

    This API provides a complete set of endpoints for developers and educators to interact with the platform programmatically,
    allowing seamless integration, extension, and customization of the educational experience.

    ## Endpoints Featured

    From this root, you can navigate to all the primary endpoints for managing various aspects of the system:

    - **Users:** `/api/users`
      Endpoints for user management, including registration, authentication, and profile operations.

    - **Categories:** `/api/categories`
      Endpoints for organizing courses into categories by subject or theme.

    - **Tags:** `/api/tags`
      Endpoints to manage tags and filter courses based on topics.

    - **Learning Paths:** `/api/paths`
      Endpoints for curated sequences of courses that guide learners through a defined study path.

    - **Courses:** `/api/courses`
      Endpoints to create, retrieve, update, and delete courses.

    - **Course Enrollments:** `/api/enrollments`
      Endpoints for managing students' enrollments in courses.

    - **Course Reviews:** `/api/reviews`
      Endpoints for submitting and moderating course reviews.

    - **Modules:** `/api/modules`
      Endpoints to manage course modules.

    - **Lessons:** `/api/lessons`
      Endpoints for handling lessons within modules.

    - **Lesson Items:** `/api/items`
      Endpoints to manage individual items within lessons.

    - **Assignments:** `/api/assignments`
      Endpoints for setting up and managing lesson assignments.

    - **Assignment Questions:** `/api/questions`
      Endpoints for creating and managing questions linked to assignments.

    - **Assignment Submissions:** `/api/submissions`
      Endpoints to handle assignment submissions and instructor grading.

    ## Usage

    Send a GET request to the API root (e.g., `/api`) to receive a JSON object listing all
    available endpoints along with their URLs. This navigational overview makes it simple for developers to explore and
    integrate the various supported features.

    ### Sample Request

    ```bash
    curl -X GET /api
    ```

    ### Sample Response

    ```json
    {
        "users": "http://127.0.0.1:8000/api/users",
        "categories": "http://127.0.0.1:8000/api/categories",
        "paths": "http://127.0.0.1:8000/api/paths",
        "courses": "http://127.0.0.1:8000/api/courses",
        "enrollments": "http://127.0.0.1:8000/api/enrollments",
        "posts": "http://127.0.0.1:8000/api/posts",
        "modules": "http://127.0.0.1:8000/api/modules",
        "reviews": "http://127.0.0.1:8000/api/reviews",
        "lessons": "http://127.0.0.1:8000/api/lessons",
        "items": "http://127.0.0.1:8000/api/items",
        "assignments": "http://127.0.0.1:8000/api/assignments",
        "questions": "http://127.0.0.1:8000/api/questions",
        "answers": "http://127.0.0.1:8000/api/answers",
        "submissions": "http://127.0.0.1:8000/api/submissions"
    }
    ```

    ## Permissions

    By design, the `APIRootView` is generally accessible to all users as it only serves as a navigational
    guide into the API and does not expose any sensitive or privileged data.
    """


class CourseInstanceAPI(APIRootView):
    """
    ## Overview

    The `CourseInstanceAPI` serves as the root entry point for all course-related endpoints within the API.
    It provides a structured, navigable representation of various functionalities associated with course interactions,
    including enrollments, announcements, modules, and reviews.

    ## Endpoints Featured

    The following endpoints are available through this API root:

    - **Enrollments:** `/api/courses/{courseId}/enrollments/`
      Manage student enrollments in courses, including registration, progress tracking, and withdrawal.

    - **Posts:** `/api/courses/{courseId}/posts/`
      Allows instructors to post announcements, updates, and course-related information.

    - **Modules:** `/api/courses/{courseId}/modules/`
      Provides access to course modules, including lesson organization and curriculum structure.

    - **Reviews:** `/api/courses/{courseId}/reviews/`
      Enables students to submit, view, and moderate course reviews.

    ## Usage

    This API root acts as a navigational map for developers and users to explore course-related functionality.
    Sending a GET request to the API root (e.g., `/api/courses/1/`) returns a JSON object
    containing all available course-related endpoints.

    ### Example Request

    ```bash
    curl -X GET /api/courses/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ### Example Response

    ```json
    {
        "enrollments": "/api/courses/1/enrollments",
        "posts": "/api/courses/1/posts",
        "modules": "/api/courses/1/modules",
        "reviews": "/api/courses/1/reviews"
    }
    ```

    ## Permissions

    - **Students:**
      Can access enrollments, posts, and reviews related to their courses.

    - **Instructors/Admins:**
      Can manage course posts, enrollments, and module configurations.

    This API root simplifies navigation and usage of course-related features within the platform,
    ensuring a streamlined experience for developers and users.
    """


class ModuleInstanceAPI(APIRootView):
    """
    ## Overview

    The `ModuleInstanceAPI` serves as the entry point for all module-related API endpoints.
    It provides structured access to functionalities within course modules, specifically managing lessons.

    ## Endpoints Featured

    The following endpoints are accessible under this API root:

    - **Lessons:** `/api/courses/{courseId}/modules/{moduleId}/lessons/`
    Manages lessons within modules, including lesson creation, retrieval, updates, and deletion.

    ## Usage

    Sending a GET request to the API root (e.g., `/api/courses/1/modules/1/`) returns a JSON object containing
    available module-related endpoints.

    ### Example Request

    ```bash
    curl -X GET /api/courses/1/modules/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ### Example Response

    ```json
    {
        "lessons": "/api/courses/1/modules/1/lessons"
    }
    ```

    ## Permissions

    - **Students:**
    Can view lessons within modules they are enrolled in.

    - **Instructors/Admins:**
    Can manage lessons by creating, updating, or deleting them.

    This API root ensures intuitive navigation within the module management system,
    making it simple for developers and users to interact with lesson-related functionalities.
    """


class LessonInstanceAPI(APIRootView):
    """
    ## Overview

    The `LessonInstanceAPI` serves as the entry point for all lesson-related API endpoints.
    It provides structured access to functionalities within lessons, including assignments and lesson items.

    ## Endpoints Featured

    The following endpoints are available under this API root:

    - **Assignments:** `/api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments`
    Manage lesson assignments, including grading and feedback.

    - **Items:** `/api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items`
    Handles various items within lessons, such as text sections, videos, quizzes, and interactive exercises.

    ## Usage

    Sending a GET request to the API root (e.g., `/api/courses/1/modules/1/lessons/1/`) returns
    a JSON object containing available lesson-related endpoints.

    ### Example Request

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ### Example Response

    ```json
    {
        "assignments": "/api/courses/1/modules/1/lessons/1/assignments",
        "items": "/api/courses/1/modules/1/lessons/1/items"
    }
    ```

    ## Permissions

    - **Students:**
    Can view lesson items and submit assignments.

    - **Instructors/Admins:**
    Can manage lesson assignments, grade submissions, and update lesson items.

    This API root simplifies lesson-related interactions, providing a structured way to manage assignments and lesson content efficiently.
    """


class AssignmentInstanceAPI(APIRootView):
    """
    ## Overview

    The `AssignmentInstanceAPI` serves as the entry point for all assignment-related API endpoints.
    It provides structured access to functionalities within assignments, including questions and student submissions.

    ## Endpoints Featured

    The following endpoints are available under this API root:

    - **Questions:** `/api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions`
      Manage assignment questions, including multiple-choice, short-answer, and coding challenges.

    - **Submissions:** `/api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions`
      Handles student assignment submissions, grading, and feedback.

    ## Usage

    Sending a GET request to the API root (e.g., `/api/courses/1/modules/1/lessons/1/assignments/1/`)
    returns a JSON object containing available assignment-related endpoints.

    ### Example Request

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1/assignments/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ### Example Response

    ```json
    {
        "questions": "/api/courses/1/modules/1/lessons/1/assignments/1/questions",
        "submissions": "/api/courses/1/modules/1/lessons/1/assignments/1/submissions"
    }
    ```

    ## Permissions

    - **Students:**
      Can view and submit assignments.

    - **Instructors/Admins:**
      Can create, update, and grade assignment submissions and questions.

    This API root streamlines assignment interactions, making it easy for students to complete coursework
    and instructors to manage assessments efficiently.
    """


class QuestionInstanceAPI(APIRootView):
    """## Overview

    The `QuestionInstanceAPI` serves as the entry point for question-related endpoints within the API.
    Specifically, it provides structured access to functionalities for managing answers to assignment or exam questions.
    This endpoint enables complete CRUD (Create, Retrieve, Update, Delete) operations on answers, supporting both
    student submissions and instructor reviews.

    ## Endpoints Featured

    - **Answers:** `/api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers`
      This endpoint allows for the submission, retrieval, updating, and deletion of answers to questions.
      It is essential for handling interactions related to assignment question answers.

    ## Usage

    Sending a GET request to the API root (e.g., `/api/courses/1/modules/1/lessons/1/assignments/1/questions/1/`)
    returns a JSON object that lists available endpoints under the questions module.

    ### Example Request

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1/assignments/1/questions/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ### Example Response

    ```json
    {
        "answers": "/api/questions/answers/"
    }
    ```

    ## Permissions

    - **Instructors/Admins:**
      Have full access to manage answers, including creating, updating, grading, and deleting answers submitted by students.

    This API root provides a streamlined interface for handling question answers, facilitating effective assessment and 
    feedback mechanisms in the educational platform.
    """
