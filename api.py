from flask import Flask, jsonify, request
from dateutil.parser import parse
from datetime import datetime


def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False


app = Flask(__name__)

events = [
    {
        "start": "",
        "stop": "",
        "tags": ["tag1", "tag2"]
    },
    {
        "start": "",
        "stop": "",
        "tags": ["tag3", "tag4"]
    }
]



@app.route("/list_events")
def list_events():
    return jsonify(data=events)


@app.route("/add_event", methods=['POST'])
def add_events():
    global events
    

    if not request.is_json:
        return jsonify({"message": "Data should be sent in json format"})
    
    json_data = request.get_json()

    if "start" not in json_data or not is_date(json_data['start']):
        return jsonify({"message": "'start' key is required and must be in date format"})
    
    if "stop" in json_data:
        if not is_date(json_data['stop']):
            return jsonify({"message": "'stop' key must be a date format"})


    if "tags" not in json_data:
        return jsonify({"message": "'tags' key is required"})

    if not isinstance(json_data['tags'], list):
        return jsonify({"message": "'tags' field must be a list of strings"})
     
    if not all(isinstance(e, str) for e in json_data['tags']):
        return jsonify({"message": "'tags' field must be a list of strings"})
    
    json_data['start'] = datetime.timestamp(parse(json_data['start']))
    if "stop" in json_data:
        json_data['stop'] = datetime.timestamp(parse(json_data['stop']))

    events.append(json_data)
    return jsonify({"message": "Event added successfully"})



@app.route("/delete_events", methods=['DELETE'])
def delete_events():
    global events
    events = []
    return jsonify({"message": "Events deleted"})


if __name__ == "__main__":
    app.run()