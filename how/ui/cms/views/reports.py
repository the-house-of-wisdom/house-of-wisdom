"""Report views"""

from wagtail.admin.views.reports import PageReportView
from wagtail.models import Page


# Create your report view here.
class UnpublishedChangesReportView(PageReportView):
    """Pages with unpublished changes"""

    page_title = "Unpublished changes"
    header_icon = "doc-empty-inverse"
    index_url_name = "unpublished_changes_report"
    index_results_url_name = "unpublished_changes_report_results"

    def get_queryset(self):
        return Page.objects.filter(has_unpublished_changes=True)
