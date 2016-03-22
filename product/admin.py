# -*- coding: utf-8 -*-
from django.contrib import admin
from product.models import Product, ProductType


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'is_available',
              'is_visible', 'height', 'width', 'product_type', 'main_image']
    list_filter = ['create_date']
    list_display = (
        'title', 'product_type', 'price', 'is_visible', 'is_available',)
    search_fields = ['title']
admin.site.register(Product, ProductAdmin)
