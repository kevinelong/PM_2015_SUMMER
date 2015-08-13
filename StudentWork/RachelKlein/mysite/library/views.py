from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Checkout
from django.shortcuts import render_to_response

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

    return render_to_response(
        'library_home.html',
        context= {
            'books': books
        }
    )