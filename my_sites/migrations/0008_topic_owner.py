# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 06:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_sites', '0007_remove_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
