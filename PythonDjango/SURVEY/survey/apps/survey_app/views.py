from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
from django.utils.crypto import get_random_string


def index(request):
    return render(request, 'survey/templates/index.html', context)


def result(request):
    # default submits to 0 so if somebody goes straight to result, don't error
    if 'submits' not in request.session:
        request.session['submits'] = 0

    context = {
        "submitsText": "Thanks for submitting this form #{} many times.)".format(request.session['attempt']),
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment'],
    }
    return render(request, 'survey/templates/index.html', context)


def processSurvey(request):
   # if submits # exists, increase it.  Otherwise initialize it to 1 because it is the first attempt
    if request.method == "POST":
        if 'submits' in request.session:
            request.session['submits'] += 1
        else:
            request.session['submits'] = 1
        print request.session['submits']
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    return redirect('/result')

# Create your views here.
