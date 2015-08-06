# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='chair',
            field=models.ForeignKey(blank=True, to='courses.Faculty', null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dept',
            field=models.ForeignKey(blank=True, to='courses.Department', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(blank=True, to='courses.Department', null=True),
        ),
    ]
