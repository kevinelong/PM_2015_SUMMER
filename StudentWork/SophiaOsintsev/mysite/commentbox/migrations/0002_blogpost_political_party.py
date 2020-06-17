# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='political_party',
            field=models.CharField(default=b'OTH', max_length=15, choices=[(b'DEM', b'Democrat'), (b'REP', b'Republican'), (b'OTH', b'Other')]),
        ),
    ]
