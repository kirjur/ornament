# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from product.models import Product, Image, Product_type
from django.core.paginator import Paginator
from django.contrib import auth
from django.template import RequestContext

# Create your views here.


def products(request, page_number=1):
    all_products = Product.objects.all()
    current_page = Paginator(all_products, 6)
    args = {}
    args['products'] = current_page.page(page_number)
    args['images'] = Image.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response('products.html', args)


def product(request, product_id=1, page_number=1, *args, **kwargs):
    context = RequestContext(request, {
        'product': Product.objects.get(id=product_id)
    })
    return render_to_response('product.html', RequestContext)
