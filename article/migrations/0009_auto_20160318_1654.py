# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160318_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 18, 16, 54, 27, 645254, tzinfo=utc)),
        ),
    ]
