from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'is_available',
              'is_visible', 'height', 'width', 'product_type', 'main_image']
    list_filter = ['create_date']
    list_display = ('title',)
admin.site.register(Product, ProductAdmin)
