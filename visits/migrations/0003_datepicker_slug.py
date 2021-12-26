# Generated by Django 3.2.10 on 2021-12-23 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_auto_20211223_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='datepicker',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
