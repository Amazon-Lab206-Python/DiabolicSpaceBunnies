# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    initializeWords(request)
    context = {
        'words': request.session['words']
    }
    return render(request, 'index.html', context)


def add(request):
    initializeWords(request)
    # checked request.POST['new_word'] to prevent blanks
    if request.method == "POST" and request.POST['new_word']:
        print request.POST
        if 'bigText' in request.POST:
            bigText = True
        else:
            bigText = False
        newWord = {
            'word': request.POST['new_word'],
            'color': request.POST['color'],
            'bigText': bigText
        }
        # Cannot directly append to request.session list
        templist = request.session['words']
        templist.append(newWord)
        request.session['words'] = templist
        print request.session['words']
        print 'banana'
    else:
        print 'no word was given'
    return redirect("/session_words")


def clear(request):
    if request.method == "POST":
        request.session['words'] = []
    return redirect("/session_words")


def initializeWords(request):
    if 'words' not in request.session:
        request.session['words'] = []

# Create your views here.
