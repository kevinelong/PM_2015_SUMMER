# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20150901_2014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Recipe',
        ),
    ]
