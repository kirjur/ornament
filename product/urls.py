from django.conf.urls import url
import product.views

urlpatterns = [
    url(r'^get/(\d+)/$', product.views.product),
    url(r'^all/$', product.views.products),
    url(r'^$', product.views.products),
]
