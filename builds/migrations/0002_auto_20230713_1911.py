# Generated by Django 3.2.20 on 2023-07-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='gallery_image_1',
            field=models.ImageField(default='../default_build_nvxeo7', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='build',
            name='gallery_image_2',
            field=models.ImageField(default='../default_build_nvxeo7', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='build',
            name='gallery_image_3',
            field=models.ImageField(default='../default_build_nvxeo7', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='build',
            name='gallery_image_4',
            field=models.ImageField(default='../default_build_nvxeo7', upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='GalleryImages',
        ),
    ]