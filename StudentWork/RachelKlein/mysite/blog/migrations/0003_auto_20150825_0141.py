# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150821_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='article',
            field=models.ForeignKey(related_name='comments', to='blog.BlogArticle', null=True),
        ),
    ]
