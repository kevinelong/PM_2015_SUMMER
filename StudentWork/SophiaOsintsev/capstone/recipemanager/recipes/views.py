from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template import RequestContext
import re
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import *
from django.contrib.auth import authenticate, login, logout
from .forms import AddRecipeForm
from .models import Recipe


def homepage(request):
    query_string = ''
    found_entries = None

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'ingredients',])

        found_entries = Recipe.objects.filter(entry_query)

        return render_to_response(
            'homepage.html',
            {'query_string': query_string, 'found_entries': found_entries},
            context_instance=RequestContext(request)
        )

    return render_to_response('homepage.html', context_instance=RequestContext(request))

@login_required
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
            'button_name': 'Add',
        }
    )

@login_required
def edit_recipe(request, recipe_id):
    recipe_entry = get_object_or_404(Recipe, id=recipe_id)

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
            'button_name': 'Edit',
        }
    )

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
    return HttpResponseRedirect(reverse('delete_successful'))


def delete_successful(request, recipe_id=None):
    recipes = get_object_or_404(Recipe, pk=recipe_id) if recipe_id else None

    return render_to_response(
        'delete_successful.html',
        context={
            'recipes': recipes,
        }
    )


def all_recipes(request):
    query_string = ''
    found_entries = None

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'ingredients',])

        found_entries = Recipe.objects.filter(entry_query)

        return render_to_response(
            'all_recipes.html',
            {'query_string': query_string, 'found_entries': found_entries},
            context_instance=RequestContext(request)
        )

    recipes = Recipe.objects.all()
    return render(
        request,
        'all_recipes.html',
        context={
            'recipes': recipes,
        }
    )

@login_required
def full_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(
        request,
        'full_recipe.html',
        context={
            'recipe': recipe,
        }
    )


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))