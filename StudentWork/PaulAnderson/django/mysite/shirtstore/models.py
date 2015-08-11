from django.db import models

class Shirt(models.Model):
    COLOR_CHOICES = (
        ('RED', 'Red'),
        ('ORA', 'Orange'),
        ('YEL', 'Yellow'),
        ('GRE', 'Green'),
        ('BLU', 'Blue'),
        ('PUR', 'Purple'),
    )

    SIZE_CHOICES = (
        ('SM', 'Small'),
        ('MED', 'Medium'),
        ('LG', 'Large'),
    )

    color = models.CharField(
        choices=COLOR_CHOICES,
        max_length=24,
    )
    size = models.CharField(
        choices=SIZE_CHOICES,
        max_length=24,
    )
    style_name = models.CharField(max_length=255)
    item_id = models.CharField(
        unique=True,
        null=False, blank=False,
        max_length=24,
    )

    def __unicode__(self):
        return '{} shirt'.format(self.style_name)


class Store(models.Model):
    name = models.CharField(max_length=50)
    available_shirts = models.ManyToManyField(Shirt)

    def __unicode__(self):
        return '{} store'.format(self.name)