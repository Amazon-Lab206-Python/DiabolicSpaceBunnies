# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "name = " + self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "name = " + self.first_name + " " + self.last_name


class Book_Author(models.Model):
    book_id = models.ForeignKey(Book, related_name="book_author")
    author_id = models.ForeignKey(Author, related_name="book_author")

    def __str__(self):
        return self.book_id + " " + self.author_id
