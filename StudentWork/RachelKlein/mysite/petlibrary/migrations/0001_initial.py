# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=b'True', blank=b'True')),
                ('fullness', models.IntegerField(default=4, null=b'True', blank=b'True')),
                ('health', models.IntegerField(default=5, null=b'True', blank=b'True')),
                ('days_old', models.IntegerField(default=2, null=b'True', blank=b'True')),
                ('happiness', models.IntegerField(default=5, null=b'True', blank=b'True')),
            ],
        ),
    ]
