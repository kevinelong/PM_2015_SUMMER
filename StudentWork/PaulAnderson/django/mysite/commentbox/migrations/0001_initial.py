# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_text', models.TextField()),
                ('political_party', models.CharField(max_length=255, choices=[(b'DEM', b'Democrat'), (b'REP', b'Republican'), (b'OTH', b'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='CommentBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_text', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('blog_post', models.ForeignKey(to='commentbox.BlogPost')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
