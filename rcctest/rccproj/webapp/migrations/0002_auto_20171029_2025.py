# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='type',
            field=models.CharField(choices=[('0', 'Road Bike'), ('1', 'Mountain Bike'), ('2', 'Hybrid Bike'), ('3', 'City Bike'), ('4', 'Others')], max_length=15),
        ),
    ]
