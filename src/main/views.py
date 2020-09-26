from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm, FormForSend, UserForm
from .models import Book, Contact, Logger, User
from .tasks import sleep_some_time_async
from .utils import clear_log_util


def add_user(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    context = {'form': form}
    return render(request, 'add_user.html', context=context)


def add_book(request):
    form = BookForm(request.POST)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    context = {'form': form}
    return render(request, 'add_book.html', context=context)


def edit_user(request, arg):
    user = get_object_or_404(User, pk=arg)
    form = UserForm(request.POST, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user_list')
    context = {
        'form': form,
        'user': user,
    }
    return render(request, "edit_user.html", context=context)


def edit_book(request, arg):
    book = get_object_or_404(Book, pk=arg)
    form = BookForm(request.POST, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book_list')
    context = {
        'form': form,
        'book': book,
    }
    return render(request, "edit_book.html", context=context)


def delete_user(request, arg):
    user = get_object_or_404(User, pk=arg)
    user.delete()
    return redirect('user_list')


def delete_book(request, arg):
    book = get_object_or_404(Book, pk=arg)
    book.delete()
    return redirect('book_list')


def clear_log(request):
    clear_log_util()
    return redirect('log')


def user_list(request):
    users = User.objects.all()
    count = users.count()
    context = {
        'title': 'Users list',
        'count': count,
        'users': users,
    }
    return render(request, 'user_list.html', context=context)


def book_list(request):
    books = Book.objects.all()
    count = books.count()
    context = {
        'title': 'Book list',
        'count': count,
        'books': books,
    }
    return render(request, 'book_list.html', context=context)


def log(request):
    notes = Logger.objects.all().order_by('-created')
    count = Logger.objects.count()
    context = {
        'title': 'Users list',
        'count': count,
        'notes': notes,
    }
    return render(request, 'Log.html', context=context)


def slow(request):
    sleep_some_time_async.delay(10)
    return render(request, 'index.html')


def send_form(request):
    form = FormForSend(request.POST)
    if request.method == 'POST':
        form = FormForSend(request.POST)
        if form.is_valid():
            form.save()
            return redirect('send_history')
    context = {'form': form}
    return render(request, 'send.html', context=context)


def send_history(request):
    notes = Contact.objects.all().order_by('-sends')
    count = Contact.objects.count()
    context = {
        'title': 'Mail list',
        'count': count,
        'notes': notes,
    }
    return render(request, 'mail_history.html', context=context)
