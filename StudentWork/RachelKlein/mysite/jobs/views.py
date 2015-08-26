from django.shortcuts import render_to_response
from forms import JobPostingForm, JobRemovalForm, NewUserForm
from .models import JobPosting
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def posting_site(request):
    posts = []
    for job in JobPosting.objects.all():
        posts.append(job)

    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posting_site'))
    else:
        form = JobPostingForm()

    context = {
        'form': form.as_p(),
        'posts': posts,
    }
    context.update(csrf(request))

    return render_to_response(
        'posting_site.html',
        context=context,

    )

@login_required
def remove_posting(request):
    if request.method == 'POST':
        form = JobRemovalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posting_site'))
    else:
        form = JobRemovalForm()

        context = {
            'form': form,
        }

        context.update(csrf(request))

        return render_to_response(
            'remove_posting.html',
            context=context,
        )

def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posting_site'))
    else:
        form = NewUserForm()

        context = {
            'form': form,
        }

        context.update(csrf(request))

        return render_to_response(
            'new_user.html',
            context=context,
        )