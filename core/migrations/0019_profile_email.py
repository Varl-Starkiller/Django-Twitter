# Generated by Django 5.0.2 on 2024-02-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_profile_coverimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]