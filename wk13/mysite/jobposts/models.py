import logging
from django.db import models

logger = logging.getLogger(__name__)


class JobPost(models.Model):
    RELIGION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    years_experience = models.IntegerField(default=0)
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, default='Y')
    likes_cats = models.BooleanField(default=True)

    post_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def is_health_insurance_qualified(self):
        """
        Return boolean based on if this position will qualify for company subsidized health insurance. Qualifications
        currently found in our company handbook which no one has.
        """
        cats_rel = self.likes_cats and self.religion == 'Y'
        exp_title = self.years_experience > 5 and 'manager' in self.title.lower()
        if cats_rel:
            logger.info('Job posting {} has cats and religion is Y'.format(self.id))
        if exp_title:
            logger.info('Job posting {} has more than 5yrs experience and has manager in title'.format(self.id))
        return cats_rel or exp_title

    def increase_experience(self, amount_increase):
        """
        Increases the experience required by the given amount.
        """
        logger.info('Increasing experience of JobPost {} from {} to {}'.format(
            self.id, self.years_experience, self.years_experience + amount_increase
        ))
        self.years_experience += amount_increase
        self.save()