# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_checkout_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='name',
        ),
    ]
