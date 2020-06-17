# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0002_blogpost_political_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_title',
            field=models.CharField(default=b'Untitled', max_length=20),
        ),
    ]
