from celery import shared_task
import time

@shared_task
def celery_task(counter):
    email = "hassanzadeh.sd@gmail.com"
    time.sleep(30)
    return '{} Done!'.format(counter)