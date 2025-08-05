"""URLConf for how.ui"""

from django.contrib.auth import views as auth
from django.urls import path

from how.ui import views

# Create your URLConf here.
app_name = "ui"


auth_urls = [
    path("accounts/login/", auth.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.SignupView.as_view(), name="signup"),
    path("accounts/profile/", views.ProfileView.as_view(), name="profile"),
    path("accounts/<int:pk>/update/", views.UserUpdateView.as_view(), name="u-user"),
    path("accounts/<int:pk>/delete/", views.UserDeleteView.as_view(), name="d-user"),
    path(
        "accounts/password/change/",
        auth.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password/change/done/",
        auth.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password/reset/",
        auth.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password/reset/done/",
        auth.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/password/reset/<uidb64>/<token>/",
        auth.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password/reset/complete/",
        auth.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]


urlpatterns = auth_urls + [
    path(
        "about/",
        views.HomeView.as_view(),
        name="about",
    ),
    path(
        "contact/",
        views.HomeView.as_view(),
        name="contact",
    ),
    path(
        "learn/",
        views.LearnView.as_view(),
        name="learn",
    ),
    path(
        "learn/<slug:course>/",
        views.CourseDetailView.as_view(),
        name="course",
    ),
    path(
        "learn/<slug:course>/grades/",
        views.CourseGradesView.as_view(),
        name="grades",
    ),
    path(
        "learn/<slug:course>/grades/<slug:assignment>/",
        views.AssignmentDetailView.as_view(),
        name="assignment",
    ),
    path(
        "learn/<slug:course>/grades/<slug:assignment>/submissions/<int:pk>/",
        views.SubmissionDetailView.as_view(),
        name="submission",
    ),
    path(
        "learn/<slug:course>-<int:id>/enroll/",
        views.EnrollmentCreateView.as_view(),
        name="enroll",
    ),
    path(
        "learn/<slug:course>-<int:id>/reviews/",
        views.CourseReviewsView.as_view(),
        name="reviews",
    ),
    path(
        "learn/<slug:course>-<int:id>/reviews/new/",
        views.ReviewCreateView.as_view(),
        name="new_review",
    ),
    path(
        "learn/<slug:course>-<int:id>/reviews/<int:pk>/",
        views.ReviewUpdateView.as_view(),
        name="update_review",
    ),
    path(
        "learn/<slug:course>/posts/",
        views.CoursePostsView.as_view(),
        name="posts",
    ),
    path(
        "learn/<slug:course>/posts/<slug:post>/",
        views.PostDetailView.as_view(),
        name="post",
    ),
    path(
        "learn/<slug:course>/<slug:module>/",
        views.ModuleDetailView.as_view(),
        name="module",
    ),
    path(
        "learn/<slug:course>/<slug:module>/<slug:lesson>/",
        views.LessonDetailView.as_view(),
        name="lesson",
    ),
    path(
        "learn/<slug:course>/<slug:module>/<slug:lesson>/<slug:item>/",
        views.ItemDetailView.as_view(),
        name="item",
    ),
]
