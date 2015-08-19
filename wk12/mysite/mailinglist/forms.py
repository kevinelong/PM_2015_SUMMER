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