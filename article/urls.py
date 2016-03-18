from django.conf.urls import url
import article.views

urlpatterns = [
    url(r'^articles/all/$', article.views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/(?P<page_number>\d+)/$', article.views.article),
    url(r'^articles/get/(?P<article_id>\d+)/$', article.views.article),
    url(r'^articles/addlike/(?P<page_number>\d+)/(?P<article_id>\d+)/$', article.views.addlike),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', article.views.addcomment),
    url(r'^page/(\d+)/$', article.views.articles),
    url(r'^$', article.views.articles),
]
