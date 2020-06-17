from django.db import models

class Gift(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        null=False, blank=False,
    )
    wedding = models.ForeignKey(
        'Wedding',
        related_name='gifts',
        null=True, blank=True,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['price']

class Wedding(models.Model):
    name = models.CharField(
        max_length=255,
    )
    date = models.DateField(
        null=False, blank=False,
    )

    def __unicode__(self):
        return self.name