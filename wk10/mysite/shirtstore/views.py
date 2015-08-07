from django.http import HttpResponse

from .models import Store


def availability(request):

    stores_list = []
    for store in Store.objects.iterator():
        shirts = ', '.join([str(s) for s in store.available_shirts.iterator()])
        store_availability_text = '{} has these shirts: {}'.format(
            store, shirts
        )
        stores_list.append(store_availability_text)

    return HttpResponse(
        'Here are the shirts available by store:<br/><br/>' + '<br/>'.join(stores_list)
    )