from django.db import models
# import datetime

class Patron(models.Model):
    card_number = models.IntegerField(
        null='True', blank='True',
    )
    name = models.CharField(
        max_length=(255),
        null='True', blank='True',
    )

    def __unicode__(self):
        return self.name

class Book(models.Model):
    ISBN = models.IntegerField(
        null='True', blank='True',
    )
    name = models.CharField(
        max_length=(255),
        null='True', blank='True',
    )

    def is_checked_out(self):
        if Checkout.objects.filter(checkout_book=self, checkin_date__isnull=True).exists():
            return True
        else:
            return False

    def __unicode__(self):
        return self.name

class Checkout(models.Model):
    checkout_date = models.DateTimeField('date checked out')
    checkin_date = models.DateTimeField(
        'date checked in'
        # Can this be null by default?
    )
    checkout_patron = models.ForeignKey(
        'Patron',
        null='True', blank='True',
    )
    checkout_book = models.ForeignKey(
        'Book',
        null='True', blank='True',
    )

    def __unicode__(self):
        return '{} checked out {}'.format(
            self.checkout_patron,
            self.checkout_book,
        )