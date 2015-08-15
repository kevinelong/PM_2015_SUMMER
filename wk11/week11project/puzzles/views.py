from django.shortcuts import render_to_response

from .models import Clue, Puzzle, PuzzleBoard


def clues_count(request):
    total_clues = Clue.objects.count()
    return render_to_response(
        'total_clues.html',
        context={
            'total_clues': total_clues,
        }
    )
