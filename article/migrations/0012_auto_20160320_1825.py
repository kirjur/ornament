# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20160320_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]