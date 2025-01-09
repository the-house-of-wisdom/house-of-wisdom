""" URLConf for BAH UI """

from django.urls import path, include

from bah_ui.views import (
    AboutView,
    IndexView,
    ProfileView,
    create,
    delete,
    detail,
    list,
    update,
)


# Create your URLConf here.
app_name = "bah-ui"

account_urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
]

admin_urlpatterns = [
    # Categories
    path(
        "categories/",
        list.CategoryListView.as_view(),
        name="categories",
    ),
    path(
        "categories/new/",
        create.CategoryCreateView.as_view(),
        name="new-category",
    ),
    path(
        "categories/<int:id>/",
        detail.CategoryDetailView.as_view(),
        name="view-category",
    ),
    path(
        "categories/<int:id>/delete/",
        delete.CategoryDeleteView.as_view(),
        name="delete-category",
    ),
    path(
        "categories/<int:id>/update/",
        update.CategoryUpdateView.as_view(),
        name="update-category",
    ),
    # Faculties
    path(
        "faculties/",
        list.FacultyListView.as_view(),
        name="faculties",
    ),
    path(
        "faculties/new/",
        create.FacultyCreateView.as_view(),
        name="new-faculty",
    ),
    path(
        "faculties/<int:id>/",
        detail.FacultyDetailView.as_view(),
        name="view-faculty",
    ),
    path(
        "faculties/<int:id>/delete/",
        delete.FacultyDeleteView.as_view(),
        name="delete-faculty",
    ),
    path(
        "faculties/<int:id>/update/",
        update.FacultyUpdateView.as_view(),
        name="update-faculty",
    ),
    # Departments
    path(
        "departments/",
        list.DepartmentListView.as_view(),
        name="departments",
    ),
    path(
        "departments/new/",
        create.DepartmentCreateView.as_view(),
        name="new-department",
    ),
    path(
        "departments/<int:id>/",
        detail.DepartmentDetailView.as_view(),
        name="view-department",
    ),
    path(
        "departments/<int:id>/delete/",
        delete.DepartmentDeleteView.as_view(),
        name="delete-department",
    ),
    path(
        "departments/<int:id>/update/",
        update.DepartmentUpdateView.as_view(),
        name="update-department",
    ),
    # Tags
    path(
        "tags/",
        list.TagListView.as_view(),
        name="tags",
    ),
    path(
        "tags/new/",
        create.TagCreateView.as_view(),
        name="new-tag",
    ),
    path(
        "tags/<int:id>/",
        detail.TagDetailView.as_view(),
        name="view-tag",
    ),
    path(
        "tags/<int:id>/delete/",
        delete.TagDeleteView.as_view(),
        name="delete-tag",
    ),
    path(
        "tags/<int:id>/update/",
        update.TagUpdateView.as_view(),
        name="update-tag",
    ),
]

instructor_urlpatterns = [  # Courses
    path("courses/", list.CourseListView.as_view(), name="courses"),
    path("courses/new/", create.CourseCreateView.as_view(), name="new-course"),
    path(
        "courses/<int:id>/",
        detail.CourseDetailView.as_view(),
        name="view-course",
    ),
    path(
        "courses/<int:id>/delete/",
        delete.CourseDeleteView.as_view(),
        name="delete-course",
    ),
    path(
        "courses/<int:id>/update/",
        update.CourseUpdateView.as_view(),
        name="update-course",
    ),
    # Items
    path("items/new/", create.ItemCreateView.as_view(), name="new-item"),
    path(
        "items/<int:id>/delete/",
        delete.ItemDeleteView.as_view(),
        name="delete-item",
    ),
    path(
        "items/<int:id>/update/",
        update.ItemUpdateView.as_view(),
        name="update-item",
    ),
    # Modules
    path("modules/new/", create.ModuleCreateView.as_view(), name="new-module"),
    path(
        "modules/<int:id>/delete/",
        delete.ModuleDeleteView.as_view(),
        name="delete-module",
    ),
    path(
        "modules/<int:id>/update/",
        update.ModuleUpdateView.as_view(),
        name="update-module",
    ),
    # Reviews
    path("reviews/new/", create.ReviewCreateView.as_view(), name="new-review"),
    path(
        "reviews/<int:id>/delete/",
        delete.ReviewDeleteView.as_view(),
        name="delete-review",
    ),
    path(
        "reviews/<int:id>/update/",
        update.ReviewUpdateView.as_view(),
        name="update-review",
    ),
    # Lessons
    path("lessons/new/", create.LessonCreateView.as_view(), name="new-lesson"),
    path(
        "lessons/<int:id>/delete/",
        delete.LessonDeleteView.as_view(),
        name="delete-lesson",
    ),
    path(
        "lessons/<int:id>/update/",
        update.LessonUpdateView.as_view(),
        name="update-lesson",
    ),
    # Specializations
    path(
        "specializations/",
        list.SpecializationListView.as_view(),
        name="specializations",
    ),
    path(
        "specializations/new/",
        create.LessonCreateView.as_view(),
        name="new-specialization",
    ),
    path(
        "specializations/<int:id>/",
        detail.SpecializationDetailView.as_view(),
        name="view-specialization",
    ),
    path(
        "specializations/<int:id>/delete/",
        delete.LessonDeleteView.as_view(),
        name="delete-specialization",
    ),
    path(
        "specializations/<int:id>/update/",
        update.LessonUpdateView.as_view(),
        name="update-specialization",
    ),
]

urlpatterns = (
    [
        path("", IndexView.as_view(), name="index"),
        path("about/", AboutView.as_view(), name="about"),
    ]
    + account_urlpatterns
    + admin_urlpatterns
    + instructor_urlpatterns
)
