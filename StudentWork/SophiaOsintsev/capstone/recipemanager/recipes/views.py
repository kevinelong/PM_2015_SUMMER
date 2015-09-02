from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AddRecipeForm, DeleteRecipeForm
from .models import Recipes


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect(reverse('full_recipe', args=[recipe.id]))

    else:
        form = AddRecipeForm()

    return render(
        request,
        'add_recipe.html',
        context={
            'form': form,
        }
    )


def edit_recipe(request, recipe_id):
    recipe_entry = get_object_or_404(Recipes, id=recipe_id)

    if request.method == 'POST':
        form = AddRecipeForm(request.POST, instance=recipe_entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('full_recipe', args=[recipe_id]))

    else:
        form = AddRecipeForm(instance=recipe_entry)

    return render(
        request,
        'add_recipe.html',
        context={
            'form': form,
        }
    )


def delete_recipe(request):
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('delete_successful'))
    else:
        form = DeleteRecipeForm()

    return render(
        request,
        'delete_recipe.html',
        context={
            'form': form
        }
    )


def delete_successful(request, recipe_id=None):
    recipes = get_object_or_404(Recipes, pk=recipe_id) if recipe_id else None

    return render_to_response(
        'delete_successful.html',
        context={
            'recipes': recipes,
        }
    )


def all_recipes(request):
    recipes = Recipes.objects.all()
    return render(
        request,
        'all_recipes.html',
        context={
            'recipes': recipes,
        }
    )


def full_recipe(request, recipe_id):
    recipes = get_object_or_404(Recipes, id=recipe_id)
    return render(
        request,
        'full_recipe.html',
        context={
            'recipes': recipes,
        }
    )

def search_recipes():
    pass
