# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from product.models import Product, Image
from settings.models import Settings
from django.core.paginator import Paginator
from django.contrib import auth
# Create your views here.


def products(request, page_number=1):
    all_products = Product.objects.all()
    current_page = Paginator(all_products, 5)
    args = {}
    args['products'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    args['settings'] = Settings.objects.all()
    return render_to_response('products.html', args)


def product(request, product_id=1, page_number=1):
    args = {}
    args['product'] = Product.objects.get(id=product_id)
    args['images'] = Image.objects.all()
    args['username'] = auth.get_user(request).username
    args['settings'] = Settings.objects.all()
    return render_to_response('product.html', args)
