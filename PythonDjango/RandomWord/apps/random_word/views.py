from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
from django.utils.crypto import get_random_string


def index(request):
    # if attempt # exists, increase it.  Otherwise initialize it to 1 because it is the first attempt
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    print request.session['attempt']
    context = {
        "attempt": "Random Word (attempt #{})".format(request.session['attempt']),
        "rando": get_random_string(length=14)
    }
    return render(request, 'random_word/index.html', context)


def reset(request):
    # TODO: reset the counter
    try:
        del request.session['attempt']
    except keyError:
        print "attempt was not in the session"
    return redirect('/random_word')
# Create your views here.
