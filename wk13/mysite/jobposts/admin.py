from django.contrib import admin

from .models import JobPost

class JobPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(JobPost, JobPostAdmin)