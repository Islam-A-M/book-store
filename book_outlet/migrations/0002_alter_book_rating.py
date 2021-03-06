# Generated by Django 3.2.8 on 2022-02-12 07:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Min rate is 1'), django.core.validators.MaxValueValidator(5, message='Max rate is 5')]),
        ),
    ]
