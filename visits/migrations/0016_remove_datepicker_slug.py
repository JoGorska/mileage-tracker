# Generated by Django 3.2.10 on 2021-12-29 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0015_datepicker_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datepicker',
            name='slug',
        ),
    ]
