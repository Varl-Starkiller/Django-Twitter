# Generated by Django 5.0.2 on 2024-02-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_post_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='post_images'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
