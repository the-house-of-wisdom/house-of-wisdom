"""Wagtail Hooks used to customize the view-level behavior of the Wagtail admin and front-end"""

from django.urls import path, reverse_lazy
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.ui.cms.views.choosers import viewsets
from bayt_al_hikmah.ui.cms.views.reports import UnpublishedChangesReportView


# Create your hooks here.
@hooks.register("register_admin_viewset")
def register_views():
    return [*viewsets.values()]


@hooks.register("construct_explorer_page_queryset")
def show_my_pages_only(parent_page, pages, request):
    """Filter pages by user"""

    page = pages.first()

    if page:
        if isinstance(page, Category):
            return pages

    return pages.filter(owner=request.user)


@hooks.register("construct_document_chooser_queryset")
def show_my_uploaded_documents_only(documents, request):
    """Filter docs by user"""

    return documents.filter(uploaded_by_user_id=request.user.id)


@hooks.register("construct_image_chooser_queryset")
def show_my_uploaded_images_only(images, request):
    """Filter images by user"""

    return images.filter(uploaded_by_user_id=request.user.id)


@hooks.register("register_reports_menu_item")
def register_unpublished_changes_report_menu_item():
    return MenuItem(
        "Unpublished changes",
        reverse_lazy("unpublished_changes_report"),
        icon_name=UnpublishedChangesReportView.header_icon,
        order=700,
    )


@hooks.register("register_admin_urls")
def register_unpublished_changes_report_url():
    return [
        path(
            "reports/unpublished-changes/",
            UnpublishedChangesReportView.as_view(),
            name="unpublished_changes_report",
        ),
        path(
            "reports/unpublished-changes/results/",
            UnpublishedChangesReportView.as_view(results_only=True),
            name="unpublished_changes_report_results",
        ),
    ]
