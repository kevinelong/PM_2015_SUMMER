from django.contrib import admin

from .models import Wedding, Gift



class WeddingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wedding, WeddingAdmin)


class GiftAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gift, GiftAdmin)