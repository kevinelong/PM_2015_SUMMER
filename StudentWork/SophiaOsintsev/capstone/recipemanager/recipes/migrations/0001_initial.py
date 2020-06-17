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
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(default=b'APP', max_length=3, choices=[(b'APP', b'Appetizer'), (b'BRK', b'Breakfast & Brunch'), (b'DES', b'Dessert'), (b'SLD', b'Salad'), (b'SOP', b'Soup'), (b'BRD', b'Bread'), (b'MND', b'Main Dish'), (b'SDD', b'Side Dish'), (b'MTP', b'Meat & Poultry'), (b'SFD', b'Seafood'), (b'DRK', b'Drink'), (b'SDW', b'Sandwich')])),
                ('prep_time', models.IntegerField(help_text=b'Give an approx time from start to finish', max_length=10, blank=True)),
                ('ingredients', models.TextField(help_text=b'One ingredient per line')),
                ('directions', models.TextField(help_text=b'One direction per line')),
            ],
        ),
    ]
