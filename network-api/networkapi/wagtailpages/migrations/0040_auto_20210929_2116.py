# Generated by Django 3.1.11 on 2021-09-29 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0039_auto_20210926_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productupdates',
            options={'ordering': ['sort_order'], 'verbose_name': 'Product Update'},
        ),
    ]
