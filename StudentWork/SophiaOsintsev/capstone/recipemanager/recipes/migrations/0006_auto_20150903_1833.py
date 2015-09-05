# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_websiteuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteuser',
            name='owner',
        ),
        migrations.DeleteModel(
            name='WebsiteUser',
        ),
    ]
