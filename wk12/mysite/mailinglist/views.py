from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import MailingList
from .forms import MailingListForm, ManyMailingListForm, DeleteListForm, CreateListForm


def add_email(request, list_id):
    mailinglist = get_object_or_404(MailingList, pk=list_id)
    header = 'Join our {} mailing list!'.format(
        mailinglist.name
    )


    if request.method == 'POST':
        form = MailingListForm(request.POST)
        if form.is_valid():
            form.save(mailinglist)
            return HttpResponseRedirect(reverse('thanks', args=[list_id]))

    else:
        form = MailingListForm()

    return render(request, 'add_email.html',
        {
            'form': form,
            'header': header,
        },
    )


def thanks(request, list_id=None):

    mailinglist = get_object_or_404(MailingList, pk=list_id) if list_id else None

    return render_to_response(
        'thanks.html',
        context={
            'list': mailinglist,
            'lists_to_join': MailingList.objects.all().exclude(id=list_id),
        }
    )


def add_email_to_many(request):
    if request.method == 'POST':
        form = ManyMailingListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thanks'))

    else:
        form = ManyMailingListForm()

    return render(request, 'add_email.html',
                  {
                      'form': form.as_p(),
                      'header': 'Join one of our {} mailing lists!'.format(
                          MailingList.objects.count()
                      ),
                  })


def delete_list(request):
    if request.method == 'POST':
        form = DeleteListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = DeleteListForm()

    return render(
        request,
        'delete.html',
        context={
            'form': form
        }
    )


def create_list(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thanks'))

    else:
        form = CreateListForm()

    return render(
        request,
        'create.html',
        context={
            'form': form,
        }
    )