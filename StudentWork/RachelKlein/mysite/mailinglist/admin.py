from django.contrib import admin

from .models import MailingList, Email



class MailingListAdmin(admin.ModelAdmin):
    pass
admin.site.register(MailingList, MailingListAdmin)


class EmailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Email, EmailAdmin)