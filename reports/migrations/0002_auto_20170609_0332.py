# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refugeereport',
            name='city_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='refugeereport',
            name='country_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='refugeereport',
            name='state_total',
            field=models.IntegerField(default=0),
        ),
    ]
