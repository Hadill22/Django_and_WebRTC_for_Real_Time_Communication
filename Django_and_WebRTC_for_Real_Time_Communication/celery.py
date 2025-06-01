# Django_and_WebRTC_for_Real_Time_Communication/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_and_WebRTC_for_Real_Time_Communication.settings')

app = Celery('Django_and_WebRTC_for_Real_Time_Communication')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()