from django.contrib import admin

from django.contrib import admin
from library.models import Book, Patron, Checkout

class PatronAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patron, PatronAdmin)

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class CheckoutAdmin(admin.ModelAdmin):
    pass
admin.site.register(Checkout, CheckoutAdmin)