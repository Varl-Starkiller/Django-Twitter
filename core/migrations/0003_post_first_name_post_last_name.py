# Generated by Django 4.2.4 on 2024-01-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_followerscount_likepost_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
