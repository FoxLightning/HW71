import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw7.settings')

app = Celery('hw7')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
