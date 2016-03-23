from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from settings import MEDIA_URL, MEDIA_ROOT
import about.views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^basicview/', include('article.urls'), name="basicview"),
    url(r'^products/', include('product.urls'), name="products"),
    url(r'^auth/', include('loginsys.urls'), name="auth"),
    url(r'^about/$', about.views.about, name="about"),
    url(r'^order/$', about.views.order, name="order"),
    url(r'^contacts/$', about.views.contacts, name="contacts"),
    url(r'^', include('article.urls'), name="index"),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
