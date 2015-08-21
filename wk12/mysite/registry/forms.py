from django import forms

from .models import Gift


class PurchaseForm(forms.Form):
    item = forms.ChoiceField(
        widget=forms.RadioSelect(),
    )

    def __init__(self, *args, **kwargs):
        self.wedding = kwargs.pop('wedding')
        super(PurchaseForm, self).__init__(*args, **kwargs)
        choices = []
        for gift in Gift.objects.filter(wedding=self.wedding):
            choice_text = '{}: ${}'.format(gift.name, gift.price)
            this_choice = (gift.id, choice_text)
            choices.append(this_choice)

        self.fields['item'].choices = choices

    def save(self):
        gift_id = self.cleaned_data['item']
        gift = Gift.objects.get(id=gift_id)
        self.wedding.gifts.remove(gift)