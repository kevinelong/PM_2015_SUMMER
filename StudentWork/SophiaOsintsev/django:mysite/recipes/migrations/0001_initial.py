# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_title', models.CharField(unique=True, max_length=255, choices=[(b'DESS', b'DESSERT'), (b'APP', b'APPETIZER'), (b'SOP', b'SOUP'), (b'MAI', b'MAIN DISH'), (b'SLD', b'SALAD'), (b'SDE', b'SIDE')])),
                ('recipe_ingredients', models.CharField(max_length=10000)),
                ('recipe_directions', models.CharField(max_length=20000)),
            ],
        ),
    ]
