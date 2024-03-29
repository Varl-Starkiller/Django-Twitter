# Generated by Django 5.0.2 on 2024-02-24 06:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_remove_post_attachment_remove_post_first_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='post_attachments'),
        ),
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
