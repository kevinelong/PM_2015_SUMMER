# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150805_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='courses.Student', null=b'True', blank=b'True'),
        ),
        migrations.AlterField(
            model_name='department',
            name='chair',
            field=models.ForeignKey(blank=b'True', to='courses.Faculty', null=b'True'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dpt',
            field=models.ForeignKey(blank=b'True', to='courses.Department', null=b'True'),
        ),
    ]
