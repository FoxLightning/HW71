from celery import shared_task

from .utils import clear_log_util, clear_old_log, send_user_by_xml, sleep_some_time, fill_book


@shared_task
def sleep_some_time_async(arg=10):
    sleep_some_time(arg)


@shared_task
def clear_log_util_async():
    clear_log_util()


@shared_task
def clear_old_log_async():
    clear_old_log()


@shared_task
def send_email_async(subject, text):
    from django.core.mail import send_mail
    send_mail(
        subject,
        text,
        'battlefieldblo@gmail.com',
        ['bogdanlisichenko@gmail.com'],
        fail_silently=False,
    )


@shared_task
def send_user_by_xml_async():
    send_user_by_xml()


@shared_task
def fill_book_async(num=100):
    fill_book(num)
