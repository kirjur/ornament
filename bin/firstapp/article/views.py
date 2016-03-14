from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.models import Article, Comments
from settings.models import Settings

# Create your views here.


def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    template = get_template('myview.html')
    html = template.render(Context({'name': view}))
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three"
    return render_to_response('myview.html', {'name': view})


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all(), 'settings': Settings.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(pk=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id), 'settings': Settings.objects.all()})
