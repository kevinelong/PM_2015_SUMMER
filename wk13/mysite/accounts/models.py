from django.db import models
from django.contrib.auth.models import User


class Musician(models.Model):
    INSTRUMENT_CHOICES = (
        ('CL', 'Clarinet'),
    )

    user = models.OneToOneField(User)
    instrument = models.CharField(
        max_length=3,
        choices=INSTRUMENT_CHOICES,
    )

    def __unicode__(self):
        return 'Musician: {}'.format(
            self.instrument,
        )