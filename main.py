import requests
import os
from _datetime import datetime

"""PARAMETERS"""
GENDER = "m"
WEIGHT_KG = 72
HEIGHT_CM = 172
AGE = 30

NUT_APP_ID = os.environ.get("NUT_APP_ID")
NUT_API_KEY = os.environ.get("NUT_API_KEY")
nut_endpoint = os.environ.get("nut_endpoint")

"""POSTING"""
user_input = input("Tell me which exercises you did:")

nut_headers = {
    "x-app-id": NUT_APP_ID,
    "x-app-key": NUT_API_KEY
}

nut_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nut_endpoint, json=nut_params, headers=nut_headers)
result = response.json()

sheet_endpoint = os.environ.get("sheet_endpoint")

sheet_params = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": result['exercises'][0]['name'].title(),
        "duration": result['exercises'][0]['duration_min'],
        "calories": result['exercises'][0]['nf_calories']
    }
}

authorization = os.environ.get('authorization')

sheet_headers = {
    "Authorization": authorization
}

response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_headers)


