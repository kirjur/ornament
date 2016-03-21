from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^basicview/', include('article.urls'), name="basicview"),
    url(r'^products/', include('product.urls'), name="products"),
    url(r'^auth/', include('loginsys.urls'), name="auth"),
    url(r'^', include('article.urls'), name="index"),
]
