# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 05:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('directory', models.FilePathField(default='/product_images/')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2016, 3, 18, 5, 49, 45, 4575, tzinfo=utc))),
                ('likes', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('date_delete', models.DateTimeField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
