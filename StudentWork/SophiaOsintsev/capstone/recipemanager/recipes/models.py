from django.db import models

class Recipe(models.Model):

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    CATEGORY_CHOICES = (
        ('APP', 'Appetizer'),
        ('BRK', 'Breakfast & Brunch'),
        ('DES', 'Dessert'),
        ('SLD', 'Salad'),
        ('SOP', 'Soup'),
        ('BRD', 'Bread'),
        ('MND', 'Main Dish'),
        ('SDD', 'Side Dish'),
        ('MTP', 'Meat & Poultry'),
        ('SFD', 'Seafood'),
        ('DRK', 'Drink'),
        ('SDW', 'Sandwich')
    )
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default='APP',
    )
    ingredients = models.TextField(
        blank=False,
        help_text='One ingredient per line'
    )
    directions = models.TextField(
        blank=False,
        help_text='One direction per line'
    )

    def __unicode__(self):
        return self.title

