# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-29 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_post_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='post_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='thread_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thread',
            name='post_count',
            field=models.IntegerField(default=0),
        ),
    ]
