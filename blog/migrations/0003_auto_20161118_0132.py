# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 01:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161117_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='dob',
            field=models.DateField(default=datetime.datetime(2016, 11, 18, 1, 32, 20, 484011)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='favorite_race',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='athlete',
            name='racing_since',
            field=models.DateField(default=datetime.datetime(2016, 11, 18, 1, 32, 39, 859951)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 11, 18, 1, 32, 52, 372540)),
            preserve_default=False,
        ),
    ]
