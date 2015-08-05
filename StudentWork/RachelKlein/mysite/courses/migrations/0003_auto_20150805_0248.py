# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150805_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, to='courses.Faculty', null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
