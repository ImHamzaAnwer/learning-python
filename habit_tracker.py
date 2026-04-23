import os
import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/gym-tracker"

graph_headers = {"X-USER-TOKEN": PIXELA_TOKEN}

date = datetime.now().strftime("%Y%m%d")
minutes = input("how many minutes you excercised?")
pixel_data = {"date": date, "quantity": minutes}

response = requests.post(graph_endpoint, json=pixel_data, headers=graph_headers)
print("Your data has been logged to pixela graph")
