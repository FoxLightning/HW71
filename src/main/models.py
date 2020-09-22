from django.db import models


class User(models.Model):
    f_name = models.CharField(max_length=100, verbose_name='First Name')
    l_name = models.CharField(max_length=100, verbose_name='Last Name')
    b_date = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, verbose_name='Phone number', default=None)

    def get_full_name(self):
        return f'{self.f_name} {self.l_name}'

    @property  # call like query to db
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    p_date = models.CharField(max_length=100, verbose_name='Publication date')

    def __str__(self):
        return self.title


class GoogleLead(models.Model):
    value = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Logger(models.Model):
    method = models.CharField(max_length=4, verbose_name='Method')
    path = models.CharField(max_length=100, verbose_name='Path')
    response_time = models.CharField(max_length=100, verbose_name="Response time")
    created = models.DateTimeField(auto_now_add=True)
