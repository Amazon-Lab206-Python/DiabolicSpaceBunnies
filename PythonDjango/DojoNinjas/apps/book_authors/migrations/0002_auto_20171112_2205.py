# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 05:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_author',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='book_author',
            old_name='book',
            new_name='book_id',
        ),
    ]
