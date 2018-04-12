from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class TwoColumnBlock(blocks.StructBlock):
    COLOUR_CHOICES = ('wjthe',
                      'black',
                      'gray')
    # background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="white")
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
    ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)

    class Meta:
        icon = 'image'