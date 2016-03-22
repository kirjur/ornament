# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class ProductType(models.Model):
    class Meta():
        db_table = 'product_types'

    name = models.CharField(max_length=200)


class Product(models.Model):
    class Meta():
        db_table = 'products'

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    likes = models.IntegerField(default=0, verbose_name="Количество лайков")
    price = models.IntegerField(default=0, verbose_name="Цена")
    date_delete = models.DateTimeField(null=True, verbose_name="Дата удаления")
    is_available = models.BooleanField(default=True, verbose_name="Наличие")
    is_visible = models.BooleanField(default=True, verbose_name="Видимость")
    height = models.IntegerField(default=0, verbose_name="Высота")
    width = models.IntegerField(default=0, verbose_name="Ширина")
    product_type = models.ForeignKey(ProductType, default=1, verbose_name="Тип товара")
    main_image = models.ForeignKey('Image', null=True, related_name="products", verbose_name="Главное изображение")


class Image(models.Model):
    class Meta():
        db_table = 'images'

    product = models.ForeignKey(Product, related_name=u"images")
    file = models.ImageField(
        upload_to='product_images', default='static/img/no_img.png')
