from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    class Meta():
        db_table = 'products'

    title = models.CharField(max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    likes = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date_delete = models.DateTimeField(blank=True)
    is_available = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)


class Image(models.Model):
    class Meta():
        db_table = 'images'

    product = models.ForeignKey(Product)
    is_main = models.BooleanField(default=False)
    directory = models.FilePathField(default='/product_images/')


class Product_type(models.Model):
    class Meta():
        db_table = 'product_types'

    product = models.ForeignKey(Product)
    name = models.CharField(max_length=200)
