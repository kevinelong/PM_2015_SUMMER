from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)