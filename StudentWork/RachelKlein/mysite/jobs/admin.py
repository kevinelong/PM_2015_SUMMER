from django.contrib import admin
from .models import JobPosting


class JobPostingAdmin(admin.ModelAdmin):
    pass
admin.site.register(JobPosting, JobPostingAdmin)