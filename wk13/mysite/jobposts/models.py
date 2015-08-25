from django.db import models


class JobPost(models.Model):
    RELIGION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    years_experience = models.IntegerField(default=0)
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, default='Y')
    likes_cats = models.BooleanField(default=True)

    post_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title