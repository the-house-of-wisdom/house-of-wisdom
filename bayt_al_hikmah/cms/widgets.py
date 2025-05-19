"""Widgets"""

from bayt_al_hikmah.cms.views.choosers import chooser_viewsets


# Create your widgets here.
CourseChooserWidget = chooser_viewsets["courses"].widget_class
