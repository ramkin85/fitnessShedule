# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0003_auto_20160124_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='EndTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='StartTime',
            field=models.TimeField(),
        ),
    ]
