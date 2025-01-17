# Generated by Django 3.1.11 on 2021-10-28 02:20

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0050_auto_20211104_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalproductpage',
            name='ai_helptext',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Helpful text around AI to show on the product page', max_length=5000),
        ),
        migrations.AlterField(
            model_name='generalproductpage',
            name='how_can_you_control_your_data',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='How does this product let you control your data?', max_length=5000),
        ),
        migrations.AlterField(
            model_name='generalproductpage',
            name='offline_use_description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Describe how this product can be used offline.', max_length=5000),
        ),
        migrations.AlterField(
            model_name='generalproductpage',
            name='track_record_details',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Describe the track record of this company here.', max_length=5000),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='how_does_it_use_data_collected',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='How does this product use the data collected?', max_length=5000),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='manage_vulnerabilities_helptext',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=5000),
        ),
    ]
