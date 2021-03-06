# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_auto_20180409_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='away', to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='teams.Team'),
            preserve_default=False,
        ),
    ]
