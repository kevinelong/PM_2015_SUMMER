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
            name='blog_article',
            field=models.ForeignKey(default=1, to='blog.BlogArticle'),
            preserve_default=False,
        ),
    ]
