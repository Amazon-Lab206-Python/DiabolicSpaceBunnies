# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')

# Create your views here.


def buy(request):
    safetyCheck(request)
    print "apple"
    print request.method
    print request.POST
    if request.method == "POST" and 'product_id' in request.POST:
        print "applepineapple"
        # turn the string into a number
        quantity = int(request.POST['quantity'])
        request.session['itemsOrdered'] += quantity
        product_id = request.POST['product_id']
        price = 0
        price = priceLookup(int(product_id))
        purchaseCost = price * quantity
        print "banana is {}".format(purchaseCost)
        request.session['purchaseCost'] = purchaseCost
        request.session['totalSpend'] += purchaseCost

    return redirect('/amadon/checkout')


def checkout(request):
    safetyCheck(request)
    context = {
        "purchaseCost": request.session['purchaseCost'],
        "totalSpend": request.session['totalSpend'],
        "itemsOrdered": request.session['itemsOrdered'],
    }
    return render(request, 'checkout.html', context)


def priceLookup(product_id):
    if product_id == 1015:
        return 10.50
    else:  # add more products
        return 0


def safetyCheck(request):
    if 'itemsOrdered' not in request.session:
        request.session['itemsOrdered'] = 0

    if 'totalSpend' not in request.session:
        request.session['totalSpend'] = 0


def clearSession(request):
    del request.session['itemsOrdered']
    del request.session['totalSpend']
    del request.session['purchaseCost']
    return redirect('/amadon')
