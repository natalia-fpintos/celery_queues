from time import sleep

from celery import Celery

celery_app = Celery('hello', broker='redis://localhost:6379/0')

celery_app.conf.task_routes = {
    'slow_tasks.*': {'queue': 'slow_tasks'},
    'quick_tasks.*': {'queue': 'quick_tasks'}
}


@celery_app.task(name="slow_tasks.sleep_wake_up_task")
def sleep_wake_up_task():
    sleep(10)
    return "I'm awake!"


@celery_app.task(name="quick_tasks.quick_nap_task")
def quick_nap_task():
    sleep(2)
    return "What a great nap!"
