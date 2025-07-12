"""Widgets"""

from how.cms.views.choosers import viewsets

# Create your widgets here.
classes = {k: v.widget_class for k, v in viewsets.items()}
