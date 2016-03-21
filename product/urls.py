from django.conf.urls import url
import product.views

urlpatterns = [
    url(r'^get/(\d+)/$', product.views.product, name="product"),
    url(r'^all/(\d+)/$', product.views.products, name="products"),
    url(r'^all/$', product.views.products, name="all"),
    url(r'^$', product.views.products, name="index"),
]
