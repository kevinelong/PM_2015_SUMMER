from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse

from .forms import JobCreateForm
from .models import JobPost


def create_post(request):
    if request.method == 'POST':
        form = JobCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('create_jobpost'))

    else:
        form = JobCreateForm()

    return render(
        request,
        'job_create.html',
        context={
            'form': form,
            'button_name': 'Add',
        }
    )


def update_post(request, job_id):
    jobpost = get_object_or_404(JobPost, id=job_id)

    if request.method == 'POST':
        form = JobCreateForm(request.POST, instance=jobpost)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_jobpost', args=[job_id]))

    else:
        form = JobCreateForm(instance=jobpost)

    return render(
        request,
        'job_create.html',
        context={
            'form': form,
            'button_name': 'Update',
        }
    )