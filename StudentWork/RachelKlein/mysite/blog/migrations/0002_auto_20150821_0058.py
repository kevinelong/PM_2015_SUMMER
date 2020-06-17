# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='article',
            field=models.ForeignKey(to='blog.BlogArticle', null=True),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
