# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "Hi, type in yoru word here!"
    return HttpResponse(response)

# Create your views here.
