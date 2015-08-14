import random
import sys

from django.core.management.base import BaseCommand
from django.db.models import Min, Max

from puzzles.models import Puzzle, Clue, PuzzleBoard


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_puzzle_boards()
        create_clues()
        create_puzzles()


def create_puzzle_boards():
    print 'Creating puzzle boards'

    print '  Deleting all old puzzle boards'
    PuzzleBoard.objects.all().delete()

    print '  Bulk creating new puzzle boards'
    PuzzleBoard.objects.bulk_create(
        [PuzzleBoard(width=i, height=j) for i in xrange(1, 101)
            for j in xrange(1, 101)]
    )

    print '  10,000 new puzzle boards created!'


def create_clues():
    print 'Creating clues'

    print '  Deleting all old clues'
    Clue.objects.all().delete()

    print '  Bulk creating new clues'
    Clue.objects.bulk_create(
        [Clue(
            text=get_random_words(3),
            direction=random.choice(Clue.DIRECTION_CHOICES)[0],
            number=random.randrange(100),
        ) for i in xrange(1000)]
    )

    print '  1000 new clues created!'


def create_puzzles():
    print 'Creating puzzles'

    print '  Deleting all old puzzles'
    Puzzle.objects.all().delete()

    print '  Bulk creating new puzzles'
    pb_min = PuzzleBoard.objects.all().aggregate(Min('id'))['id__min']
    pb_max = PuzzleBoard.objects.all().aggregate(Max('id'))['id__max']
    Puzzle.objects.bulk_create([
        Puzzle(
            name=get_random_words(1),
            difficulty=random.choice(Puzzle.DIFFICULTY_CHOICES)[0],
            puzzle_board_id=random.randint(pb_min, pb_max),
        ) for i in xrange(1000)
    ])

    sys.stdout.write('  Assigning clues to newly created puzzles')
    sys.stdout.flush()
    all_clues = Clue.objects.all()
    cnt = 0
    for puzzle in Puzzle.objects.iterator():
        puzzle.clues.add(*random.sample(all_clues, 5))
        cnt += 1
        if cnt % 10 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()

    print '\n  1000 new puzzles created!'


def get_random_words(num=1):
    words = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in xrange(num):
        word = ''.join([random.choice(alphabet) for j in xrange(10)])
        words.append(word)
    return ' '.join(words)
