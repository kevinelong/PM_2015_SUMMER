from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Checkout
from django.shortcuts import render_to_response
from forms import BookRequestForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf

def index(request):

    things_checked_out = Checkout.objects.count()

    books = ''
    for book in Book.objects.all():
        if not book.is_checked_out():
            books += ("<br>" + book.name)

    reminders = ''
    for checkout_event in Checkout.objects.all():
        patron = checkout_event.checkout_patron.name
        book = checkout_event.checkout_book.name
        checkout_date = checkout_event.checkout_date
        reminders += \
            ("<br>" + "{} checked out {} on {}.".format(patron, book, checkout_date))

    return HttpResponse(

        "{} books are currently checked out. And you could check out one too, for example: {}".format(
            things_checked_out, books)

        # "If you want to remind your friends when to bring their books back, here's some helpful info: {}".format(reminders)
)

def library(request):

    books = []
    for book in Book.objects.all():
        books.append(book)

    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('library_home'))
    else:
        form = BookRequestForm()

    context = {
        'form': form.as_p(),
        'books': books,
    }
    context.update(csrf(request))

    return render_to_response(
        'library_home.html',
        context=context,

    )


