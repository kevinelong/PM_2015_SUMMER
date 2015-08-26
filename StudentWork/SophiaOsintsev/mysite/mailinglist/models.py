from django.db import models


class MailingList(models.Model):
    name = models.CharField(max_length=20)
    emails = models.ManyToManyField('Email', related_name='mailing_list')

    def __unicode__(self):
        return 'MailingList "{}" with {} emails'.format(
            self.name, self.emails.count())

    class Meta:
        ordering = ['name']


class Email(models.Model):
    email_address = models.EmailField()

    def __unicode__(self):
        return self.email_address