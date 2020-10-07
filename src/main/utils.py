import datetime
from io import BytesIO
from time import sleep

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.db.utils import IntegrityError

from faker import Faker

import pytz

import xlwt

from .models import Book, Category, Logger, User


fake = Faker()


def sleep_some_time(arg=10):
    sleep(arg)


def clear_log_util():
    Logger.objects.all().delete()


def clear_old_log():
    date = datetime.datetime.now(pytz.timezone('UTC')) - datetime.timedelta(days=7)
    Logger.objects.filter(created__lt=date).delete()


def send_email_util(subject, text):
    send_mail(
        subject,
        text,
        'battlefieldblo@gmail.com',
        ['bogdanlisichenko@gmail.com',
         'dmytro.kaminskyi92@gmail.com'],
        fail_silently=False,
    )


def send_user_by_xml():
    # create excel file
    excelfile = BytesIO()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')
    # query
    fields = User._meta.fields
    qs = User.objects.all()
    # write name if field
    for col, field in enumerate(fields):
        ws.write(0, col, field.verbose_name)
    # write rows
    for row, cortege in enumerate(qs, 1):
        for col, field in enumerate(fields):
            ws.write(row, col, getattr(cortege, field.name))
    wb.save(excelfile)
    # send email
    email = EmailMessage()
    email.subject = 'User list'
    email.body = 'All date from date base about Users'
    email.from_email = 'battlefieldblo@gmail.com'
    email.to = ['bogdanlisichenko@gmail.com']
    email.attach('User_list.xls', excelfile.getvalue(), 'application/ms-excel')
    email.send()


def fill_book(number=100):
    category_n = Category.objects.count()
    l_n = category_n if category_n <= number else number
    category = list(Category.objects.order_by('?')[:l_n])
    users = list(User.objects.order_by('?'))
    user_num = len(users)
    for _ in range(number):
        book = Book.objects.create(title=fake.word(),
                                   p_date=fake.date(),
                                   category=category[fake.random_int(min=0, max=(l_n - 1), step=1)],)
        book.authors.add(*[users[fake.random_int(min=0, max=(user_num-1), step=1)]
                           for _ in range(fake.random_int(min=1, max=4, step=1))])
        book.save()


def fill_user(number=100):
    for _ in range(number):
        try:
            User.objects.create(f_name=fake.first_name(),
                                l_name=fake.last_name(),
                                b_date=fake.date_between(start_date='-90y', end_date='-10y'),
                                email=fake.email(),
                                phone=fake.msisdn())
        except IntegrityError:
            continue


def fill_category(number=10):
    for _ in range(number):
        Category.objects.create(name=fake.word())
