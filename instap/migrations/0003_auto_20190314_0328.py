# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 00:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instap', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='content',
        ),
        migrations.RemoveField(
            model_name='image',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='image',
            name='image_pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/', upload_to='profile_pics/'),
        ),
    ]