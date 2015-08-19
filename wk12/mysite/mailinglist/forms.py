from django import forms

from .models import MailingList, Email


class MailingListForm(forms.Form):
    email_address = forms.EmailField(
        initial='reina@example.com',
        required=True,
        label='What\'s your addy?',
        help_text='if you enter your address we will spam you...',
    )

    def save(self):
        # get the value of `email_address` from the form
        email = self.cleaned_data['email_address']

        # use that value to create a new Email object in the db
        new_email = Email.objects.create(email_address=email)

        # find the list to add the email address to
        list = MailingList.objects.first()

        # add it!
        list.emails.add(new_email)