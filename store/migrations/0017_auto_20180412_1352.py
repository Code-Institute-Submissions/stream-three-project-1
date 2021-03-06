# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_cart_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='postage',
            field=models.DecimalField(decimal_places=2, default=4.99, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=4.99, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Cap', 'Cap'), ('Jersey', 'Jersey')], max_length=25),
        ),
    ]
