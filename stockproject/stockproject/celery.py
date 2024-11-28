import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')

app=Celery('stockproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule={
    'get_stock_data_1s':{
        'task': 'stocks.tasks.update_stock',
                   'schedule': 1.0}
}

app.autodiscover_tasks()