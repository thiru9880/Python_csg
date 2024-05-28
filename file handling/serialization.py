import json

data = {
    "name": "john",
    "age": 45,
    "city": "new york"
}


json_data = json.dumps(data)
print(json_data)