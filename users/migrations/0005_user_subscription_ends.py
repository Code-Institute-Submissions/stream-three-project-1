# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscription_ends',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]