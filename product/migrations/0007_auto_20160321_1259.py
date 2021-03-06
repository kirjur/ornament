# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160320_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='directory',
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=models.ImageField(default='static/img/no_img.png', upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
