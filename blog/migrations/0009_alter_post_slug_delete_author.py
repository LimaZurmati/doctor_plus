# Generated by Django 4.2.13 on 2024-06-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
