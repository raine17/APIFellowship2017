# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-14 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20170612_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCityCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.State')),
            ],
        ),
    ]
