from django.conf.urls import url
import article.views

urlpatterns = [
    url(r'^articles/all/$', article.views.articles, name="articles"),
    url(r'^articles/get/(?P<article_id>\d+)/(?P<page_number>\d+)/$', article.views.article, name="article_comments_page"),
    url(r'^articles/get/(?P<article_id>\d+)/$', article.views.article, name="article"),
    url(r'^articles/addlike/(?P<page_number>\d+)/(?P<article_id>\d+)/$', article.views.addlike, name="article_addlike"),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', article.views.addcomment, name="article_addcomment"),
    url(r'^page/(\d+)/$', article.views.articles, name="articles_page"),
    url(r'^$', article.views.articles, name="index"),
]
