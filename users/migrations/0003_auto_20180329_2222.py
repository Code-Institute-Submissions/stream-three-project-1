# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180328_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/users'),
        ),
    ]
