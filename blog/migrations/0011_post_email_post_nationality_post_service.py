# Generated by Django 4.2.13 on 2024-06-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_language_alter_post_slug_post_languages_spoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='post',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='service',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
