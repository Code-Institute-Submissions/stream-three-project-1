# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_auto_20180403_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_team',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
