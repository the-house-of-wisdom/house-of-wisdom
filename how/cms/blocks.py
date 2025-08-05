"""Custom blocks StreamField"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock
from wagtailcodeblock.blocks import CodeBlock


# Create your blocks here.
class Code(CodeBlock):
    """Custom code block"""

    class Meta:
        icon = "code"
        template = "ui/blocks/code.html"
        form_classname = "code-block struct-block"
        form_template = "wagtailcodeblock/code_block_form.html"


class TextBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    code = Code(help_text=_("Code"))
    paragraph = blocks.RichTextBlock(help_text=_("Rich Text"))


class MediaBlock(TextBlock):
    """Custom StreamBlock for Text and Media content"""

    video = EmbedBlock(help_text=_("Video"))
    image = ImageBlock(help_text=_("Image"))
    quote = blocks.BlockQuoteBlock(help_text=_("Quote"))
    document = DocumentChooserBlock(help_text=_("Document"))
