import time

import requests

start_time = time.perf_counter()
for i in range(10):
    requests.get('http://127.0.0.1:5000/hello')
    requests.get('http://127.0.0.1:5000/sleep_request')
end_time = time.perf_counter()

print(f"Total time: {end_time - start_time}")


start_time = time.perf_counter()
for i in range(10):
    requests.get('http://127.0.0.1:5000/hello')
    requests.get('http://127.0.0.1:5000/sleep_request_async')
end_time = time.perf_counter()

print(f"Total time: {end_time - start_time}")
