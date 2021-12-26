# Generated by Django 3.2.10 on 2021-12-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatePicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_picked', models.DateField()),
                ('date_slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]
