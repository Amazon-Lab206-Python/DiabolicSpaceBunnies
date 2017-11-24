# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import User, Author, Book, Review
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


def index(request):
    return render(request, "Belt_app/index.html")


def register(request):
    result = User.objects.validate_reg(request.POST)
    if result["success"] == False:
        for error in result["errors"]:
            messages.error(request, error)
        return redirect("/")
    else:
        user_id = request.session['user_id'] = result['user'].id
        return redirect("/users/" + str(user_id))


def login(request):
    result = User.objects.validate_login(request.POST)
    if result["success"] == False:
        for error in result['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.get(
            email=request.POST['email']).id
        return redirect("/users/{}".format(request.session['user_id']))


def logout(request):
    if 'user_id' not in request.session:
        messages.error(request, "please sign in before doing that")
        return redirect("/")
    del request.session['user_id']
    return redirect('/')


def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "Belt_app/create_book.html", context)


def add_review_from_book(request, book_id):
    if 'user_id' not in request.session:
        messages.error(request, "please sign in before doing that")
        return redirect("/")
    user_id = request.session['user_id']
    book = Book.objects.get(id=book_id)
    book_data = {
        'title': book.title,
        'author': book.author,
        'existing_author': book.author.name,
        'rating': request.POST['rating'],
        'review': request.POST['review']
    }
    print book_data
    print type(book.author)
    result = Review.objects.validate_review(book_data, user_id)
    if result['success'] == False:
        for error in result['errors']:
            messages.error(request, error)
    return redirect("/books/" + book_id)


def books(request):
    if 'user_id' not in request.session:
        messages.error(request, "please sign in before doing that")
        return redirect("/")

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'recent': Review.objects.all().order_by('-created_at')[:3],
        'more': Review.objects.all().order_by('-created_at')[3:]
    }
    return render(request, "Belt_app/books.html", context)


def create_book(request):
    if 'user_id' not in request.session:
        messages.error(request, "please sign in before doing that")
        return redirect("/")
    user_id = request.session['user_id']
    print request.POST
    result = Review.objects.validate_review(request.POST, user_id)
    if result['success'] == False:
        for error in result['errors']:
            messages.error(request, error)
        return redirect("/books/add")
    else:
        book_id = result['review'].book.id
        return redirect("/books/{}".format(book_id))


def book_page(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'reviews': Review.objects.filter(book=book_id)
    }
    return render(request, "Belt_app/book_page.html", context)


def delete_review(request, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect("/books")


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids = user.reviews.all().values("book").distinct()
    unique_books = []
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    context = {
        'user': user,
        'unique_books': unique_books
    }
    return render(request, "Belt_app/user_page.html", context)
