from time import sleep

from flask import Flask

from celery_app import sleep_wake_up_task, quick_nap_task

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/sleep_request')
def sleep_wake_up():
    sleep(5)
    return "I'm awake!"


@app.route('/sleep_request_async')
def sleep_wake_up_async():
    sleep_wake_up_task.delay()
    return 'Sleeping...'


@app.route('/nap_request_async')
def nap_async():
    quick_nap_task.delay()
    return 'Nap time...'


if __name__ == '__main__':
    app.run()
