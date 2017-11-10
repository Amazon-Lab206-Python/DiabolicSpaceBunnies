# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last)_name=models.CharField(max_length = 255)
    email=models.EmailField(unique = True)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)

    def ___str___(self):
        return self.email
