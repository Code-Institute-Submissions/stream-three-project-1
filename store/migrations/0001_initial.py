# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0004_auto_20180326_1050'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Cap', 'Cap'), ('Jersey', 'Jersey'), ('Hoodie', 'Hoodie')], max_length=25)),
                ('description', models.CharField(max_length=10)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=25)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/store/')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ManyToManyField(related_name='products', to='store.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
