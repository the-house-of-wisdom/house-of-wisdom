"""Wagtail Hooks used to customize the view-level behavior of the Wagtail admin and front-end"""

from wagtail import hooks

from bayt_al_hikmah.cms.views.choosers import chooser_viewsets
from bayt_al_hikmah.cms.views.groups import AdminViewSetGroup, InstructorViewSetGroup
from bayt_al_hikmah.cms.views.sets import PathViewSet


# Create your hooks here.
@hooks.register("register_admin_viewset")
def register_views():
    return [
        PathViewSet("paths"),
        AdminViewSetGroup(),
        InstructorViewSetGroup(),
        *chooser_viewsets.values(),
    ]


# @hooks.register("filter_form_submissions_for_user")
# def construct_forms_for_user(user, queryset):
#     if not user.is_superuser:
#         queryset = queryset.none()
#     return queryset


# @hooks.register("construct_page_chooser_queryset")
# def show_my_pages_only(pages, request):
#     """Filter pages by user"""
#     return pages.filter(owner=request.user)


@hooks.register("construct_document_chooser_queryset")
def show_my_uploaded_documents_only(documents, request):
    """Filter docs by user"""

    return documents.filter(uploaded_by_user_id=request.user.id)


@hooks.register("construct_image_chooser_queryset")
def show_my_uploaded_images_only(images, request):
    """Filter images by user"""

    return images.filter(uploaded_by_user_id=request.user.id)
