# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0006_lessonclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientApi',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shedule.Client')),
            ],
            bases=('shedule.client',),
        ),
        migrations.AddField(
            model_name='client',
            name='Comment',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='client',
            name='State',
            field=models.CharField(default='ACTIVE', max_length=15),
        ),
        migrations.AddField(
            model_name='lesson',
            name='State',
            field=models.CharField(default='ACTIVE', max_length=20),
        ),
    ]
