# Generated by Django 3.2.10 on 2021-12-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0014_alter_journey_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='datepicker',
            name='slug',
            field=models.SlugField(default=2000, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]