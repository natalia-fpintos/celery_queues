from time import sleep

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/sleep_request')
def sleep_wake_up():
    sleep(5)
    return "I'm awake!"


if __name__ == '__main__':
    app.run()
