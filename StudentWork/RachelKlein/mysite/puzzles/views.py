from django.shortcuts import render_to_response
from .models import Clue, Puzzle, PuzzleBoard
from .forms import NewPuzzleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf

def welcome(request):
    total_puzzles = Puzzle.objects.count()
    return render_to_response(
        'welcome.html',
        context={
            'total_puzzles': total_puzzles,
        }
    )

def clues_count(request):
    total_clues = Clue.objects.count()
    return render_to_response(
        'total_clues.html',
        context={
            'total_clues': total_clues,
        }
    )

def small_width(request):
    small_width_puzzles = Puzzle.objects.filter(puzzle_board__width__lte=10)
    return render_to_response(
        'small_width.html',
        context={
            'small_width_puzzles': small_width_puzzles,
        }
    )

def devilish(request):
    devilish_puzzles = Puzzle.objects.filter(difficulty='DE')
    return render_to_response(
        'devilish.html',
        context={
            'devilish_puzzles': devilish_puzzles,
        }
    )

def easy_n(request):
    easy_n_puzzles = Puzzle.objects.filter(difficulty='EA', name__startswith='n')
    return render_to_response(
        'easy_n.html',
        context={
            'easy_n_puzzles': easy_n_puzzles,
        }
    )

def not_ten(request):
    not_ten_puzzles = Puzzle.objects.exclude(puzzle_board__width=10, puzzle_board__height=10)
    return render_to_response(
        'not_ten.html',
        context={
            'not_ten_puzzles': not_ten_puzzles,
        }
    )

def puzzles_by_clue(request):
    clue = Clue.objects.first()   # We could randomize this later, or make it user input.
    puzzles = clue.puzzle_set.all()
    return render_to_response(
        'puzzles_by_clue.html',
        context={
            'puzzles_by_clue': puzzles,
        }
    )

def suggest_puzzle(request):
    if request.method == 'POST':
        form = NewPuzzleForm(request.POST)
        if form.is_valid:
            #save to list of new puzzles
            form.save()
            return HttpResponseRedirect('welcome')
    else:
        form = NewPuzzleForm()

    context = {
        'form': form.as_p(),
    }
    context.update(csrf(request))

    return render_to_response(
        'suggest_puzzle.html',
        context=context,
    )

