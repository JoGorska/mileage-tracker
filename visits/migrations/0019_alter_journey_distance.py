# Generated by Django 3.2.10 on 2022-01-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0018_auto_20220108_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, verbose_name='Distance Travelled'),
        ),
    ]
