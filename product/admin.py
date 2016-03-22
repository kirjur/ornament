from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'is_available',
              'is_visible', 'height', 'width', 'product_type', 'main_image']
    inlines = [Product]
    # list_filter = ['date']
    list_display = ('product_type', 'title')
admin.site.register(Product)
