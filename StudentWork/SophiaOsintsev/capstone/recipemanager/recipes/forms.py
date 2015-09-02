from django import forms

from .models import Recipes


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        exclude = []


class DeleteRecipeForm(forms.Form):
    recipe = forms.ChoiceField(
        label='Delete Recipe',
    )

    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)
        choices = [
            (recipe.id, recipe.title) for recipe in Recipes.objects.all()
        ]
        self.fields['recipe'].choices = choices

    def save(self):
        recipe_id = self.cleaned_data['recipe']
        recipe = Recipes.objects.get(id=recipe_id)
        recipe.delete()

