# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.IntegerField(null=b'True', blank=b'True')),
                ('name', models.CharField(max_length=255, null=b'True', blank=b'True')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkout_date', models.DateTimeField(verbose_name=b'date checked out')),
                ('checkout_book', models.ForeignKey(blank=b'True', to='library.Book', null=b'True')),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_number', models.IntegerField(null=b'True', blank=b'True')),
                ('name', models.CharField(max_length=255, null=b'True', blank=b'True')),
            ],
        ),
        migrations.AddField(
            model_name='checkout',
            name='checkout_patron',
            field=models.ForeignKey(blank=b'True', to='library.Patron', null=b'True'),
        ),
    ]
