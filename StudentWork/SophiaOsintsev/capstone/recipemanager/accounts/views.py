from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from .forms import UserForm


def register(request):

    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
    else:
        user_form = UserForm()
    return render_to_response(
        'register.html',
        {'user_form': user_form, 'registered': registered},
        context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('homepage')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {}, {}".format(username, password)
            return HttpResponse("Invalid login details")

    else:
        return render_to_response('registration/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/homepage/')


def reset(request):
    return password_reset(request, template_name='registration/password_reset_form.html',
                          email_template_name='registration/password_reset_email.html',
                          subject_template_name='registration/password_reset_subject.txt',
                          post_reset_redirect=reverse('login'))


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request,
                                  template_name='registration/password_reset_confirm.html',
                                  uidb64=uidb64,
                                  token=token,
                                  post_reset_redirect=reverse('reset_complete')
                                  )
def reset_complete(request):
    return render_to_response(
        'registration/password_reset_complete.html',)
