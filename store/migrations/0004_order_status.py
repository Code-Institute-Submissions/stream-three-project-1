# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=25),
        ),
    ]
