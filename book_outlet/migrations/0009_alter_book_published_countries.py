# Generated by Django 3.2.8 on 2022-02-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_auto_20220216_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(related_name='books', to='book_outlet.Country'),
        ),
    ]
