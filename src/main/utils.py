import datetime
from io import BytesIO
from time import sleep

from django.core.mail import EmailMessage
from django.core.mail import send_mail


import pytz

import xlwt


from .models import Logger, User


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
