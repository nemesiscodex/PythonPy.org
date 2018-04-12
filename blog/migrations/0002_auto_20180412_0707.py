# Generated by Django 2.0.3 on 2018-04-12 07:07

import datetime
from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock((('left_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock())), icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock())), icon='arrow-right', label='Right column content'))))), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('custom_table', wagtail.core.blocks.StructBlock((('custom_table', wagtail.core.blocks.StreamBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('table_intro', wagtail.core.blocks.RichTextBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'colHeaders': True, 'height': 108, 'language': 'en', 'rowHeaders': True, 'startCols': 6, 'startRows': 7})), ('footnote', wagtail.core.blocks.CharBlock(required=False))))),)))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Post date'),
        ),
    ]