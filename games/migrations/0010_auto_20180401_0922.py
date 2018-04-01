# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_auto_20180401_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='season',
            field=models.ForeignKey(default=2018, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.Season'),
        ),
    ]
