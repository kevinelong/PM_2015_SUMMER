# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('hunger', models.IntegerField(default=0)),
                ('sleepiness', models.IntegerField(default=0)),
                ('excitement', models.IntegerField(default=3)),
                ('age', models.IntegerField(default=0)),
                ('alive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('animal_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='virtualpet.Animal')),
            ],
            bases=('virtualpet.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('animal_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='virtualpet.Animal')),
            ],
            bases=('virtualpet.animal',),
        ),
    ]
