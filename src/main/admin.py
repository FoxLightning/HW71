from django.contrib import admin  # noqa

from .models import Book, Category, Contact, GoogleLead, Logger, User


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(GoogleLead)
admin.site.register(Logger)
admin.site.register(User)
