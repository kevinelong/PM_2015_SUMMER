from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .forms import ChangePasswordForm, CreateUserForm


# do not use this! there is a better way! (just this one --v )
def change_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('jobs_list'))

    else:
        form = ChangePasswordForm(instance=user)

    return render(
        request,
        'change_password.html',
        context={
            'form': form,
            'user': user,
        }
    )


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(
        request,
        'user_detail.html',
        context={
            'this_user': user,
        }
    )


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('user_detail', args=[new_user.id]))

    else:
        form = CreateUserForm()

    return render(
        request,
        'create_user.html',
        context={
            'form': form,
        }
    )