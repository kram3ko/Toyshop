# Generated by Django 5.1.7 on 2025-04-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='customer',
        ),
        migrations.AddField(
            model_name='user',
            name='shop_admin',
            field=models.BooleanField(default=False),
        ),
    ]
