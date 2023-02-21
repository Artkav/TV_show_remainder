import os

from celery import Celery
# from app.tasks import print_20_sec

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'show_remainder.settings')

app = Celery('show_remainder')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task
def add(x, y):
    z = x + y
    print(z)


#
# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.add',
#         'schedule': 30.0,
#         'args': (5, 3),
#     },
# }
# app.conf.timezone = 'UTC'


# app.add_periodic_task(20, print_20_sec.s(), name='add-every-20-seconds')

