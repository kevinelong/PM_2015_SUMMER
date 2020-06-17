# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', null=b'True', blank=b'True'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(blank=b'True', to='courses.Department', null=b'True'),
        ),
    ]
