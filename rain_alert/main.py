import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


ACCOUNT_SID = os.getenv("TWILIO_ACC_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
API_KEY = os.getenv("OWM_API_KEY")

LAT = 40.978931
LNG = 27.515240


def send_sms():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Its going to rain today, Chatri lelena ☂️",
        to="+92000000000",
        from_="+19783070637",
    )
    print(message.sid)


response = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LNG}&cnt=4&appid={API_KEY}"
)
response.raise_for_status()
weather_data = response.json()["list"]

for forecast in weather_data:
    if forecast["weather"][0]["id"] < 700:
        send_sms()
        break
