# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobposts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='likes_cats',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='religion',
            field=models.CharField(default=b'Y', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='years_experience',
            field=models.IntegerField(default=0),
        ),
    ]
