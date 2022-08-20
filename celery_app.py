from time import sleep

from celery import Celery

celery_app = Celery('hello', broker='redis://localhost:6379/0')


@celery_app.task
def sleep_wake_up_task():
    sleep(10)
    return "I'm awake!"
