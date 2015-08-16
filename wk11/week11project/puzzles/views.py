from django.shortcuts import render_to_response, get_object_or_404

from .models import Clue, Puzzle, PuzzleBoard


def clues_count(request):
    total_clues = Clue.objects.count()
    return render_to_response(
        'total_clues.html',
        context={
            'total_clues': total_clues,
        }
    )


def home_page(request):
    return render_to_response('home.html')


def clues_width_less_than(request, width):
    clues = Clue.objects.filter(puzzle__puzzle_board__width__lte=width).distinct()
    return render_to_response(
        'clues_width_less_than.html',
        context={
            'clues': clues,
            'width': width,
        }
    )


def devilish_clues(request):
    clues = Clue.objects.filter(puzzle__difficulty='DE').distinct()
    return render_to_response(
        'devilish_clues.html',
        context={
            'clues': clues,
        }
    )


def clue_detail(request, clue_id):
    clue = get_object_or_404(Clue, id=clue_id)
    return render_to_response(
        'clue_detail.html',
        context={
            'clue': clue,
        }
    )


def puzzle_detail(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, id=puzzle_id)
    return render_to_response(
        'puzzle_detail.html',
        context={
            'puzzle': puzzle,
        }
    )


def clues_list(request):
    return render_to_response(
        'clue_list.html',
        context={
            'clues': Clue.objects.all(),
        }
    )