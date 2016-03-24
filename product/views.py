# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from product.models import Product
from django.template import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth



def products(request, page_number=1, *args, **kwargs):
    all_products = Product.objects.all()
    current_page = Paginator(all_products, 6)
    context = RequestContext(request, {
        'user': auth.get_user(request),
        'all_products': current_page.page(request.GET.get('page', page_number)),
    })
    # page_number = request.GET.get('page')
    # try:
    #     all_products = current_page.page(page_number)
    # except PageNotAnInteger:
    #     all_products = current_page.page(1)
    # except EmptyPage:
    #     all_products = current_page.page(current_page.num_pages)
    return render_to_response('products.html', context)


def product(request, product_id=1, page_number=1, *args, **kwargs):
    context = RequestContext(request, {
        'user': auth.get_user(request),
        'product': Product.objects.get(id=product_id),
    })
    return render_to_response('product.html', context)
