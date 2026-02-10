import json

import requests

r = "http://127.0.0.1:8000"
get_response = requests.get(r)

print("Status Code: ", get_response.status_code)
print("Response JSON: ", get_response.json())

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

r = "http://127.0.0.1:8000/data/"
post_response = requests.post(r, json=data)

print("Status Code: ", post_response.status_code)
print("Response JSON: ", post_response.json())
