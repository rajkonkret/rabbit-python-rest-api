from pprint import pprint

import requests
import json

user = 'guest'
password = 'guest'
server = 'http://localhost:15672'


def get_queues():
    response = requests.get(f'{server}/api/queues', auth=(user, password))
    if response.status_code == 200:
        print(response.text)
        return response.json()
    else:
        return f"Error: {response.status_code}"


def create_queue(queue_name):
    data = {
        "auto_delete": False,
        "durable": True
    }
    response = requests.put(f'{server}/api/queues/%2F/{queue_name}',
                            auth=(user, password),
                            headers={"Content-Type": "application/json"},
                            data=json.dumps(data))
    if response.status_code == 204:
        return f"Queue {queue_name} created succcesaafully"
    else:
        return f"Error: {response.status_code}"


queues = get_queues()
print("Queues:", queues)
print(type(queues))
for q in queues:
    print(q['name'])
    print(q['auto_delete'])

result = create_queue("my_new_queue")
print(result)
