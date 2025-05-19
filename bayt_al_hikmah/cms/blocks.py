"""Custom blocks StreamField"""

from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from bayt_al_hikmah.cms.views.choosers import chooser_viewsets


# Create your blocks here.
class TextContentBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    paragraph = blocks.RichTextBlock()
    heading = blocks.CharBlock(form_classname="title")


class CommonContentBlock(TextContentBlock):
    """Custom StreamBlock for Text and Media content"""

    image = ImageChooserBlock()
    document = DocumentChooserBlock()


CourseChooserBlock = chooser_viewsets["courses"].get_block_class(
    name="CourseChooserBlock",
    module_path="cms.blocks",
)
