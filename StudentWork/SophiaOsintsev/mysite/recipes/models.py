from django.db import models

class Recipe(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        default=0,
    )

    recipe_ingredients = models.TextField(
        null=False,
        blank=False,
    )

    recipe_directions = models.TextField(
        null=False,
        blank=False,
    )
    def __unicode__(self):
        return self.name
