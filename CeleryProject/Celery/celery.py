import os
from time import sleep

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery.settings')

app = Celery('Celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.worker_pool = 'solo'


# Load task modules from all registered Django apps.
app.autodiscover_tasks()

#Task
@app.task(name = 'add')
def add(x, y):
    sleep(10)
    return x + y

#@app.task(bind=True, ignore_result=True)
#def debug_task(self):
#    print(f'Request: {self.request!r}')