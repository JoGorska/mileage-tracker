# Generated by Django 3.2.10 on 2021-12-23 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visits', '0006_auto_20211223_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='datepicker',
            name='driver',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='date_picker', to='auth.user'),
            preserve_default=False,
        ),
    ]
