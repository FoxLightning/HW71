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
    date = datetime.datetime.now(pytz.timezone('Europe/Kiev')) - datetime.timedelta(days=7)
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
    qs = User.objects.all()
    excelfile = BytesIO()

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    ws.write(0, 0, 'ID')
    ws.write(0, 1, 'First Name')
    ws.write(0, 2, 'Last Name')
    ws.write(0, 3, 'Date of birth')
    ws.write(0, 4, 'Email')
    ws.write(0, 5, 'Phone number')

    for num, cortege in enumerate(qs):
        num += 1
        ws.write(num, 0, cortege.id)
        ws.write(num, 1, cortege.f_name)
        ws.write(num, 2, cortege.l_name)
        ws.write(num, 3, cortege.b_date.strftime("%d %m %Y"))
        ws.write(num, 4, cortege.email)
        ws.write(num, 5, cortege.phone)

    wb.save(excelfile)

    email = EmailMessage()
    email.subject = 'User list'
    email.body = 'All date from date base about Users'
    email.from_email = 'battlefieldblo@gmail.com'
    email.to = ['bogdanlisichenko@gmail.com',
                'dmytro.kaminskyi92@gmail.com']
    email.attach('User_list.xls', excelfile.getvalue(), 'application/ms-excel')
    email.send()
