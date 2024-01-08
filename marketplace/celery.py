from celery import Celery
import os

# Настройки для celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')

app = Celery('service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()