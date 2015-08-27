import logging

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import JobCreateForm
from .models import JobPost

logger = logging.getLogger(__name__)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = JobCreateForm(request.POST)
        if form.is_valid():
            job = form.save()
            logger.debug('New job post created, has id {}'.format(job.id))
            return HttpResponseRedirect(reverse('job_detail', args=[job.id]))

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


@login_required
def update_post(request, job_id):
    jobpost = get_object_or_404(JobPost, id=job_id)

    if request.method == 'POST':
        form = JobCreateForm(request.POST, instance=jobpost)
        if form.is_valid():
            form.save()
            logger.debug('Job post with id {} successfully updated'.format(job_id))
            return HttpResponseRedirect(reverse('job_detail', args=[job_id]))

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


def jobs_list(request):
    jobs = JobPost.objects.all()
    return render(
        request,
        'jobs_list.html',
        context={
            'jobs': jobs,
        }
    )


@login_required
def delete_post(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    if request.method == 'POST':
        job.delete()
        logger.debug('Job posting with id {} deleted'.format(job_id))
    return HttpResponseRedirect(reverse('jobs_list'))


def job_detail(request, job_id):
    logger.info('hello world!')
    job = get_object_or_404(JobPost, id=job_id)
    return render(
        request,
        'job_detail.html',
        context={
            'job': job,
        }
    )
