from django import forms

class NewPuzzleForm(forms.Form):
    new_puzzle_suggestion = forms.CharField(label='Suggest a Puzzle', max_length=255)