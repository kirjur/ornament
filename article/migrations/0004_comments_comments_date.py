# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160316_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 14, 0, 7, 987576, tzinfo=utc)),
        ),
    ]