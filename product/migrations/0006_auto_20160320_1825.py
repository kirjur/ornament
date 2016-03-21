# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20160318_1656'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_type',
            new_name='ProductType',
        ),
        migrations.RemoveField(
            model_name='image',
            name='is_main',
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]