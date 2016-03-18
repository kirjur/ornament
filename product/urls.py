from django.conf.urls import url
import product.views

urlpatterns = [
    url(r'^products/(\d+)/$', product.views.product),
    url(r'^products/all/$', product.views.products),
]
