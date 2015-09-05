from django import forms

from .models import Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = []


# class DeleteRecipeForm(forms.Form):
#     recipe = forms.ChoiceField(
#         label='Delete Recipe',
#     )
#
#     def __init__(self, *args, **kwargs):
#         super(DeleteRecipeForm, self).__init__(*args, **kwargs)
#         choices = [
#             (recipe.id, recipe.title) for recipe in Recipe.objects.all()
#         ]
#         self.fields['recipe'].choices = choices
#
#     def save(self):
#         recipe_id = self.cleaned_data['recipe']
#         recipe = Recipe.objects.get(id=recipe_id)
#         recipe.delete()
#
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

