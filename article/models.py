# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    class Meta():
        db_table = 'article'

    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    text = models.TextField(verbose_name="Текст комментария")
    article = models.ForeignKey(Article)
    date = models.DateTimeField(default=timezone.now)
    user_from = models.ForeignKey(User)
