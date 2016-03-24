from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth


def contacts(request, *args, **kwargs):
    context = RequestContext(request, {
        'user': auth.get_user(request),
    })
    return render_to_response('contacts.html', context)


def about(request, *args, **kwargs):
    context = RequestContext(request, {
        'user': auth.get_user(request),
    })
    return render_to_response('about.html', context)


def order(request, *args, **kwargs):
    context = RequestContext(request, {
        'user': auth.get_user(request),
    })
    return render_to_response('order.html', context)
