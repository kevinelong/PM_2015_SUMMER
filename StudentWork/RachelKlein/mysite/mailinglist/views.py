from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import MailingList
from .forms import MailingListForm, MultipleMailingListForm


def add_email(request, list_id):
    mailinglist = get_object_or_404(MailingList, pk=list_id)

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
            'list': mailinglist,
        },
    )


def thanks(request, list_id):
    mailinglist = get_object_or_404(MailingList, pk=list_id)

    return render_to_response(
        'thanks.html',
        context={
            'list': mailinglist,
            'lists_to_join': MailingList.objects.all().exclude(id=list_id),
        }
    )

def multiple_lists(request):

    if request.method == 'POST':
        form = MailingListForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('multiple_lists'))

    else:
        form = MultipleMailingListForm()

    return render(request, 'multiple_lists.html',
        {
            'form': form,
        },
    )