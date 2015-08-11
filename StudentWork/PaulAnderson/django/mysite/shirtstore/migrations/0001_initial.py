# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=24, choices=[(b'RED', b'Red'), (b'ORA', b'Orange'), (b'YEL', b'Yellow'), (b'GRE', b'Green'), (b'BLU', b'Blue'), (b'PUR', b'Purple')])),
                ('size', models.CharField(max_length=24, choices=[(b'SM', b'Small'), (b'MED', b'Medium'), (b'LG', b'Large')])),
                ('style_name', models.CharField(max_length=255)),
                ('item_id', models.CharField(unique=True, max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('available_shirts', models.ManyToManyField(to='shirtstore.Shirt')),
            ],
        ),
    ]
