from django.contrib import admin

from .models import Shirt, Store


class ShirtAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shirt, ShirtAdmin)


class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)