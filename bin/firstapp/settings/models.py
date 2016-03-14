from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Settings(models.Model):
    class Meta():
        db_table = 'settings'

    shop_name = models.TextField()
    main_title = models.TextField()