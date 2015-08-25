from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=30)
    posting = models.TextField()

