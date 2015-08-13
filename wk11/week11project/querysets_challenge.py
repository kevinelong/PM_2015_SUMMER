import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'week11project.settings'

import django
django.setup()

from puzzles.models import PuzzleBoard, Puzzle, Clue


# Create PuzzleBoards for all sizes with width 1-100 and height 1-100
for i in xrange(1, 101):
    for j in xrange(1, 101):
        PuzzleBoard.objects.get_or_create(width=i, height=j)


# Given a Clue, return all Puzzles that use that Clue
clue = Clue.objects.first()
clue.puzzle_set.all()


# Get all Clues that are used by Puzzles that have a width of 10 or less
Clue.objects.filter(puzzle__puzzle_board__width__lte=10)


# Get all Clues that are used in Puzzles that are ranked "Devilish"
Clue.objects.filter(puzzle__difficulty='DE')


# Get all Puzzles that have difficulty level "Easy" and whose name starts with the letter N
Puzzle.objects.filter(difficulty='EA', name__startswith='N')


# Get the count of the number of Clues currently in your database
Clue.objects.count()


# Get all Puzzles that are not of size 10 by 10
Puzzle.objects.exclude(puzzle_board__width=10, puzzle_board__height=10)