# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

# Create your models here.


class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = []
        name = postData['name']
        if len(name) < 2 or not name.isalpha():
            errors.append(
                "Name must be more than 2 characters and letters only")
        if len(postData['alias']) < 2:
            errors.append("Alias must be more than 2 characters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email was not properly formed")
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters long")
        if postData['password'] != postData['confirm_pass']:
            errors.append("confirmation password did not match")
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("This email address is already in use.")
        if len(errors) > 0:
            return {
                'success': False,
                'errors': errors
            }
        else:
            pw_hash = bcrypt.hashpw(
                postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                name=postData['name'], alias=postData['alias'], email=postData['email'], password=pw_hash)
            return {
                'success': True,
                'user': user
            }

    def validate_login(self, postData):
        errors = []
        if len(postData['email']) == 0:
            errors.append("Please provide your email address")
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Please provide a valid email address")
        if len(postData['password']) == 0:
            errors.append("Please provide your password")
        if len(User.objects.filter(email=postData['email'])) == 0:
            errors.append("email could not be found")
        if not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()):
            errors.append("invalid password")
        if len(errors) > 0:
            return {
                'success': False,
                'errors': errors
            }
        else:
            return {
                'success': True,
                'user': User.objects.get(email=postData['email'])
            }


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ReviewManager(models.Manager):
    def validate_review(self, postData, user_id):
        errors = []
        if len(postData['title']) < 1:
            errors.append("Book Title is Required.")
        if type(postData['author']) != Author:
            if len(postData['author']) < 3:
                errors.append(
                    "Author must be at least 3+ characters in length.")
        if len(postData['review']) < 1:
            errors.append("Please provide your review.")
        if len(errors) > 0:
            return {
                "success": False,
                "errors": errors
            }
        else:
            if type(postData['author']) != Author:
                if len(Author.objects.filter(name=postData['author'])) > 0:
                    author = Author.objects.get(name=postData['author'])
                else:
                    author = Author.objects.create(name=postData['author'])
            else:
                author = Author.objects.get(name=postData['existing_author'])
            if len(Book.objects.filter(title=postData['title'])) >= 1:
                book = Book.objects.get(title=postData['title'])
            else:
                book = Book.objects.create(
                    title=postData['title'], author=author)
            review = Review.objects.create(
                body=postData['review'], rating=postData['rating'], book=book, reviewer=User.objects.get(id=user_id))
            return {
                "success": True,
                "review": review
            }


class Review (models.Model):
    book = models.ForeignKey(Book, related_name="reviews")
    body = models.TextField(max_length=5000)
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    def __str__(self):
        return self.body + ' ' + self.reviewer.email
