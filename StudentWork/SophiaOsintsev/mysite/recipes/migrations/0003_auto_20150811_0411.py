# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150811_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default=0, unique=True, max_length=255),
        ),
    ]
