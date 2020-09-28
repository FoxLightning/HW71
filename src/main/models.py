from django.db import models


class User(models.Model):
    f_name = models.CharField(max_length=100, verbose_name='First Name')
    l_name = models.CharField(max_length=100, verbose_name='Last Name')
    b_date = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(unique=True)

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
