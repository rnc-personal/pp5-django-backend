# Generated by Django 3.2.20 on 2023-10-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20230730_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
