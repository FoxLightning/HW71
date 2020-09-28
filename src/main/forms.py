from django import forms

from .models import Book, Contact, User
from .tasks import send_email_async


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'b_date', 'email', 'phone']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'p_date']


class FormForSend(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'text']

    def save(self):
        subject = self.cleaned_data['subject']
        text = self.cleaned_data['text']
        send_email_async.delay(subject, text)
        super().save()
