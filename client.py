import requests


# list events
res = requests.get('http://127.0.0.1:5000/list_events')
print (res.json())

# add event
json_item = {
    "start": "Fri, 26 Mar 2021 17:29:08 GMT",
    "stop": "Fri, 26 Mar 2021 17:29:18 GMT",
    "tags": ["tag2"]
}
res = requests.post('http://127.0.0.1:5000/add_event', json=json_item)
print (res.json())

# delete events
res = requests.delete('http://127.0.0.1:5000/delete_events')
print (res.json())

# get events
res = requests.get('http://127.0.0.1:5000/list_events')
print (res.json())
