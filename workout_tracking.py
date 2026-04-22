from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

NAE_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


def add_data_to_sheet(payload):
    data = {"workout": payload}
    headers = {"Content-Type": "application/json"}
    requests.post(os.getenv("SHEETY_ENDPOINT"), json=data, headers=headers)


def get_calories():
    user_input = input("What excercise you did today ?")
    excerise_payload = {"query": user_input}

    headers = {
        "x-app-id": os.getenv("NAE_APP_ID"),
        "x-app-key": os.getenv("NAE_API_KEY"),
    }
    res = requests.post(NAE_ENDPOINT, json=excerise_payload, headers=headers)
    exercises = res.json()["exercises"]

    for excercise in exercises:
        data = {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": excercise["name"],
            "duration": excercise["duration_min"],
            "calories": excercise["nf_calories"],
        }
        add_data_to_sheet(data)


get_calories()
