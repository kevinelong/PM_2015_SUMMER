# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150805_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, to='courses.Faculty', null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='chair',
            field=models.ForeignKey(blank=True, to='courses.Faculty', null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department_name',
            field=models.ForeignKey(blank=True, to='courses.Department', null=True),
        ),
    ]
