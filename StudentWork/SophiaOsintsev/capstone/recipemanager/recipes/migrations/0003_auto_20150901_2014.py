# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_prep_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Recipes',
        ),
    ]
