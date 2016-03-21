# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from product.models import Product
from django.template import RequestContext

# Create your views here.


def products(request, page_number=1, *args, **kwargs):
    context = RequestContext(request, {
        'all_products': Product.objects.all()
    })
    return render_to_response('products.html', context)


def product(request, product_id=1, page_number=1, *args, **kwargs):
    context = RequestContext(request, {
        'product': Product.objects.get(id=product_id)
    })
    return render_to_response('product.html', context)
