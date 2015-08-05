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

    def __unicode__(self):
        return self.name

class Checkout(models.Model):
    checkout_date = models.DateTimeField('date checked out')
    checkout_patron = models.ForeignKey(
        'Patron',
        null='True', blank='True',
    )
    checkout_book = models.ForeignKey(
        'Book',
        null='True', blank='True',
    )
    name = models.CharField(
        max_length=(255),
        null='True', blank='True',
    )

    def __unicode__(self):
        return self.name