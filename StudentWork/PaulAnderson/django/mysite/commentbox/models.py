from django.db import models
from django.contrib.auth.models import User

class CommentBox(models.Model):
   comment_date = models.DateTimeField(
       auto_now_add=True,
   )
   comment_text = models.TextField(
       null=False,
       blank=False,
   )
   approved = models.BooleanField(
       default=False,
   )
   blog_post = models.ForeignKey('BlogPost')
   user = models.ForeignKey(User)

class BlogPost(models.Model):
    POLITICAL_PARTY_CHOICES = (
        ('DEM', 'Democrat'),
        ('REP', 'Republican'),
        ('OTH', 'Other'),
    )

    blog_text = models.TextField()
    political_party = models.CharField(
        choices=POLITICAL_PARTY_CHOICES,
        max_length=255,
    )


