# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20160318_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]