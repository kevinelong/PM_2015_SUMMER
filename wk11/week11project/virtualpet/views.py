from django.shortcuts import render_to_response

from .models import Animal

def animals_list(request, animal_id=None):
    return render_to_response(
        'animal_list.html',
        context={
            'animals': Animal.objects.all(),
        }
    )
