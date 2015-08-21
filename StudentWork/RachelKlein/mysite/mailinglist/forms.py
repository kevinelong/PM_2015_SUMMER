from django import forms

from .models import MailingList, Email


class MailingListForm(forms.Form):
    email_address = forms.EmailField()

    def save(self, mailinglist):
        # get the value of `email_address` from the form
        email = self.cleaned_data['email_address']

        # use that value to create a new Email object in the db
        new_email, _ = Email.objects.get_or_create(email_address=email)

        # add it to the mailing list!
        mailinglist.emails.add(new_email)

class MultipleMailingListForm(forms.Form):

    email_address = forms.EmailField()

    chosen_lists = forms.MultipleChoiceField(widget=forms.SelectMultiple,
                                             choices=all_lists)

    def __init__(self, *args, **kwargs):
        super(MultipleMailingListForm, self).init(*args, **kwargs)
        all_lists = []
        for mailinglist in MailingList.objects.iterator():
            all_lists.append((mailinglist.id, mailinglist.name))
            self.fields['chosen_lists'].choices = all_lists


    def save(self):

        email = self.cleaned_data['email_address']
        lists = self.cleaned_data['chosen_lists']

        new_email, _ = Email.objects.get_or_create(email_address=email)

        for this_list in lists:
            this_list.emails.add(new_email)