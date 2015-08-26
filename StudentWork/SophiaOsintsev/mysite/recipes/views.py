from django.http import HttpResponse

from .models import Recipe

def view_recipe(request):

    title = ''
    ingredients = ''
    directions = ''
    for recipe in Recipe.objects.all():
            title += recipe.name
            ingredients += recipe.recipe_ingredients
            directions += recipe.recipe_directions


    return HttpResponse(
        "Here are all the recipes currently saved: <br/><br/> {} <br/><br/> {} <br/><br/> {}".format(title, ingredients, directions)
    )