# Generated by Django 5.0.2 on 2024-02-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_rename_follower_followingscount_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followingscount',
            old_name='following',
            new_name='following_user',
        ),
    ]
