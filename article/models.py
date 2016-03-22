# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    class Meta():
        db_table = 'article'
        verbose_name = "Статья"

    title = models.CharField(max_length=200, verbose_name="Заголовок статьи")
    text = models.TextField(verbose_name="Текст статьи")
    date = models.DateTimeField(verbose_name="Дата статьи")
    likes = models.IntegerField(default=0, verbose_name="Количество лайков")


class Comments(models.Model):
    class Meta():
        db_table = 'comments'
        verbose_name = "Комментарий"

    text = models.TextField(verbose_name="Текст комментария")
    article = models.ForeignKey(Article, verbose_name="Статья")
    date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата комментария")
    user_from = models.ForeignKey(User, verbose_name="Пользователь")
