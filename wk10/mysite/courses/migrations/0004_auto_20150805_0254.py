# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150805_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(blank=True, to='courses.Department', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='number',
            field=models.IntegerField(default=101),
        ),
    ]
