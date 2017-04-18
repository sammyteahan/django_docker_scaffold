from celery import Celery

from django.conf import settings
from django.core.urlresolvers import reverse_lazy

app = Celery('apps.core.tasks', broker=settings.BROKER_URL)
app.conf.update(settings.CELERY_SETTINGS)


@app.task
def hello_world():
    print('Hello World')
