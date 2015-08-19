from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


from .forms import MailingListForm


def add_email(request):

    if request.method == 'POST':
        form = MailingListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mailinglist/thanks')

    else:
        form = MailingListForm()

    return render_to_response(
        'add_email.html',
        {'form': form},
        RequestContext(request),
    )


def thanks(request):
    return render_to_response(
        'thanks.html',
    )