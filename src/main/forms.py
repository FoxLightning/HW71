from django.forms import ModelForm


from .models import Book, User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'b_date', 'email']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'p_date']
