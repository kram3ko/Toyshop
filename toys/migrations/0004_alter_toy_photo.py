# Generated by Django 5.2 on 2025-04-09 09:45

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("toys", "0003_alter_toy_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="toy",
            name="photo",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format=None,
                keep_meta=True,
                null=True,
                quality=75,
                scale=None,
                size=[250, 250],
                upload_to="toys/",
            ),
        ),
    ]
