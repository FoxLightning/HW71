from django.contrib import admin  # noqa
from .models import *

admin.site.register(User)
admin.site.register(Book)
admin.site.register(GoogleLead)
admin.site.register(Logger)
admin.site.register(Contact)
admin.site.register(Category)
