# Generated by Django 3.2.20 on 2023-09-23 10:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('builds', '0003_auto_20230722_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='user_rating_1',
            field=models.ManyToManyField(blank=True, editable=False, related_name='user_rating_1', to=settings.AUTH_USER_MODEL),
        ),
    ]
