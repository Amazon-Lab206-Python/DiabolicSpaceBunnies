# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "Hi, I'm a bunny, and this is a request!"
    return HttpResponse(response)
