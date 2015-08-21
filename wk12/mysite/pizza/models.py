from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    toppings = models.ManyToManyField('Topping', blank=True)

    def __unicode__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)

    def __unicode__(self):
        return self.name