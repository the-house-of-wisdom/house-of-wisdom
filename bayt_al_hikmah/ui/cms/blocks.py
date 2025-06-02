"""Custom blocks StreamField"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from bayt_al_hikmah.ui.cms.views.choosers import viewsets


# Create your blocks here.
class TextContentBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    heading = blocks.CharBlock(form_classname="name", help_text=_("Heading"))
    paragraph = blocks.RichTextBlock(help_text=_("Rich Text"))


class CommonContentBlock(TextContentBlock):
    """Custom StreamBlock for Text and Media content"""

    image = ImageChooserBlock(help_text=_("Image"))
    document = DocumentChooserBlock(help_text=_("Document"))


PathChooserBlock = viewsets["paths"].get_block_class(
    name="PathChooserBlock",
    module_path="bayt_al_hikmah.ui.cms.blocks",
)

CourseChooserBlock = viewsets["courses"].get_block_class(
    name="CourseChooserBlock",
    module_path="bayt_al_hikmah.ui.cms.blocks",
)


class PrerequisitesBlock(blocks.StreamBlock):
    """A block for course prerequisites"""

    heading = blocks.CharBlock(form_classname="name", help_text=_("Title"))
    description = blocks.RichTextBlock(help_text=_("Description"))


class PathPrerequisitesBlock(PrerequisitesBlock):
    """A block for learning path prerequisites"""

    prerequisites = blocks.ListBlock(PathChooserBlock(), help_text=_("Prerequisites"))


class CoursePrerequisitesBlock(PrerequisitesBlock):
    """A block for course prerequisites"""

    prerequisites = blocks.ListBlock(CourseChooserBlock(), help_text=_("Prerequisites"))
