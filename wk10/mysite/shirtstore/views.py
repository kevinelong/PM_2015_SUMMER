from django.http import HttpResponse

from .models import Store

def availability(request):
    stores_list =[]
    for store in Store.objects.all():
        shirts = ''
        for shirt in store.available_shirts.all():
            shirts += ' , ()'.format(shirt)



