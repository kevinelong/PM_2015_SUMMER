from django.shortcuts import render
from django.http import HttpResponse
from .models import Shirt, Store

def index(request):

    all_shirts_everywhere = ''
    for store in Store.objects.all():
        list_of_shirts = ''
        for shirt in store.available_shirts.all():
            list_of_shirts += ("<br>" + shirt.style_name)
        store_inventory = 'At the {}, these shirts are available: {} '.format(store, list_of_shirts)
        all_shirts_everywhere += ("<br>" + store_inventory)

    return HttpResponse("Hi! Welcome to the shirt store. {}".format(all_shirts_everywhere))