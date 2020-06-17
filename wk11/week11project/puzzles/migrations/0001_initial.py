# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=1, choices=[(b'A', b'Across'), (b'D', b'Down')])),
                ('text', models.CharField(max_length=255)),
                ('number', models.IntegerField(help_text=b'The location of the clue on the board')),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('difficulty', models.CharField(max_length=3, choices=[(b'EA', b'Easy'), (b'INT', b'Intermediate'), (b'HA', b'Hard'), (b'DE', b'Devilish')])),
                ('clues', models.ManyToManyField(to='puzzles.Clue')),
            ],
        ),
        migrations.CreateModel(
            name='PuzzleBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.IntegerField(default=15)),
                ('height', models.IntegerField(default=15)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='puzzleboard',
            unique_together=set([('width', 'height')]),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='puzzle_board',
            field=models.ForeignKey(to='puzzles.PuzzleBoard'),
        ),
    ]
