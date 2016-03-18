from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Product_type(models.Model):
    class Meta():
        db_table = 'product_types'

    name = models.CharField(max_length=200)


class Product(models.Model):
    class Meta():
        db_table = 'products'

    title = models.CharField(max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date_delete = models.DateTimeField(null=True)
    is_available = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    product_type = models.ForeignKey(Product_type,default=1)


class Image(models.Model):
    class Meta():
        db_table = 'images'

    product = models.ForeignKey(Product)
    is_main = models.BooleanField(default=False)
    directory = models.FilePathField(default='/product_images/')
