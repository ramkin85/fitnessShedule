# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=True, verbose_name='ID')),
                ('DayOfWeek', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=20)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
                ('PlacesCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=True, verbose_name='ID')),
                ('Name', models.CharField(unique_for_date=True, max_length=200)),
                ('Phone', models.CharField(unique_for_date=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=True, verbose_name='ID')),
                ('Name', models.CharField(unique_for_date=True, max_length=200)),
                ('Info', models.CharField(max_length=2000)),
                ('Foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='Trainer',
            field=models.ForeignKey(to='shedule.Trainer'),
        ),
    ]
