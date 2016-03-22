from django.contrib import admin
from product.models import Product, ProductType, Image

# Register your models here.


# class ProductInLine(admin.StackedInline):
#     model = Product
#     extra = 2


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'is_available', 'is_visible', 'height', 'width', 'product_type', 'main_image']
    inlines = [Product]
    list_filter = ['date']

admin.site.register(Product)
