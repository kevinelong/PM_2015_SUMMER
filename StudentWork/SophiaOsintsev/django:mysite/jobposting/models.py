from django.db import models


class JobPosting(models.Model):
    company_name = models.ForeignKey(
        User,
        null=False, blank=False
    )
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(null=False, blank=False)

    def __unicode__(self):
        return self.title