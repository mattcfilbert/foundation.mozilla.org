# Generated by Django 3.1.11 on 2021-10-07 18:28

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0048_productpage_time_researched'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='tips_to_protect_yourself',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]