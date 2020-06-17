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


class ManyMailingListForm(forms.Form):
    email_address = forms.EmailField()
    mailinglists = forms.MultipleChoiceField(
        label='Mailing lists',
        help_text='Choose as many or as few as you\'d like!',
    )

    def __init__(self, *args, **kwargs):
        super(ManyMailingListForm, self).__init__(*args, **kwargs)
        mailinglist_choices = []
        for mailinglist in MailingList.objects.iterator():
            mailinglist_choices.append((mailinglist.id, mailinglist.name))
        self.fields['mailinglists'].choices = mailinglist_choices

    def save(self):
        email = self.cleaned_data['email_address']
        mailinglist_ids = self.cleaned_data['mailinglists']

        new_email, _ = Email.objects.get_or_create(email_address=email)
        for mailinglist_id in mailinglist_ids:
            mailinglist = MailingList.objects.get(id=mailinglist_id)
            mailinglist.emails.add(new_email)