# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170609_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='all_countries',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.City'),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='city_total',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='country_total',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.State'),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='state_total',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='refugeereport',
            name='year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]