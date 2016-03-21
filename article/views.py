# -*- coding: utf-8 -*-

from django.http.response import Http404
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
# Нужно поправить, будет изменено в версии 1.10
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth


def articles(request, page_number=1, *args, **kwargs):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 5)
    args = {}
    args['articles'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)


def article(request, article_id=1, page_number=1, *args, **kwargs):
    comment_form = CommentForm
    all_comments = Comments.objects.filter(article_id=article_id)
    current_comments_page = Paginator(all_comments, 5)
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = current_comments_page.page(page_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, page_number, article_id, *args, **kwargs):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 5)
    page = current_page.page(page_number)
    try:
        if article_id in request.COOKIES:
            redirect('/page/%s/' % page.number)
        else:
            article = Article.objects.get(id=article_id)
            article.likes += 1
            article.save()
            response = redirect('/page/%s/' % page.number)
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/page/%s/' % page.number)


def addcomment(request, article_id, *args, **kwargs):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(id=article_id)
            comment.user_from_id = auth.get_user(request).id
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)
