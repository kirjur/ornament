from django.conf.urls import url
import settings.views

urlpatterns = [
    url(r'^$', settings.views.settings),
]
