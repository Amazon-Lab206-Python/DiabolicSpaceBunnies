from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime


def index(request):
    context = {
        "time": strftime("%b %d, %Y", localtime()),
        "time2": strftime("%I:%M %p", localtime())
    }
    return render(request, 'time2_app/page.html', context)
# Create your views here.
