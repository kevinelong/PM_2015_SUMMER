# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150805_0254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
