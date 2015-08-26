from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf

from .forms import NewUserForm


def add_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add_user'))
    else:
        form = NewUserForm()

    context = {
        'form': form.as_p(),
    }
    print context
    context.update(csrf(request))
    print context

    return render_to_response(
        'new_user_page.html',
        context=context,
    )

def template_fun(request):
    return render_to_response(
        'template_fun.html',
        context={
            'list_var': ['sophia', 'vlad', 'azaiah'],
            'link': "https://google.com",
            True: "yeah",
            False: "nah",
            None: "mmmm",
            'dict_var': {}
        }
    )