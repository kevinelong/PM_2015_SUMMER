# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_directions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.TextField(),
        ),
    ]
