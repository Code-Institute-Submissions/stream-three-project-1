# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180404_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
