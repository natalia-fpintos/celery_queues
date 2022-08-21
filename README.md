# Celery with queues

## Set up

1. This repository uses Python 3.10

2. Create a virtual environment and install requirements to try locally

        $ pyenv virtualenv 3.10.2 queues
        $ pyenv activate queues
        $ pip install -r requirements.txt


3. Install Redis

        $ brew install redis


## Instructions

1. Start the Flask server to start serving requests

        $ python ./app.py

2. In another terminal window, start Redis as your Celery broker (your task queue)

        $ redis-server

3. In another terminal window, start your first Celery worker to execute tasks from the first queue

        $ celery -A celery_app worker --concurrency 6 -Q slow_tasks --log-level=INFO

4. In another terminal window, start your second Celery worker to execute tasks from the second queue

        $ celery -A celery_app worker --concurrency 6 -Q quick_tasks --log-level=INFO

5. In another terminal window, call the script to execute requests to the server

        $ python ./server_calls.py

6. You will see the output for the following simulations:
   1. Calling the endpoints without queues
   2. Calling the endpoints using a single queue
   3. Calling the endpoints using multiple queues

7. While the script runs, you can monitor the Celery worker terminal windows to see how tasks are received and executed
