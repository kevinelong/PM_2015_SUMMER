from django.http import HttpResponse

from .models import Store

def inventory(request):
    store_name = Store
    store_inventory = Store.available_shirts

    return HttpResponse(
        '{} has {} shirts available.'.format(store_name, store_inventory)
    )
