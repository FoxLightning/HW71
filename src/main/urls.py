from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    path('user_list/', views.user_list, name='user_list'),
    path('book_list/', views.book_list, name='book_list'),
    path('log/', views.log, name='log'),
    path('clear_log/', views.clear_log, name='clear_log'),

    path('add_user/', views.add_user, name='add_user'),
    path('add_book/', views.add_book, name='add_book'),

    path('edit_user/<int:arg>', views.edit_user, name='edit_user'),
    path('edit_book/<int:arg>', views.edit_book, name='edit_book'),

    path('delete_user/<int:arg>', views.delete_user, name='delete_user'),
    path('delete_book/<int:arg>', views.delete_book, name='delete_book'),

    path('slow/', views.slow, name='slow'),

    path('send/', views.send_form, name='send'),
    path('send_history/', views.send_history, name='send_history'),

    path('categories/', views.categories, name='categories'),
]
