from django.db import models
from django.contrib.auth.models import User

class JobPosting(models.Model):
    title = models.CharField(max_length=30)
    posting = models.TextField()

class Goal(models.Model):
    GOAL_CATEGORIES = (
        ('FN', 'Financial'),
        ('FT', 'Fitness'),
    )
    user = models.OneToOneField(User)
    goal_type = models.CharField(
        max_length=3,
        choices=GOAL_CATEGORIES,
    )

    def __unicode__(self):
        return '{}, which is a great kind of goal if you ask me!'.format(
            self.goal_type,
        )
