# Generated by Django 3.2.8 on 2022-02-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
