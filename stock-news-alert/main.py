import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACC_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
API_KEY = os.getenv("OWM_API_KEY")
STOCK_KEY = os.getenv("ALPHA_ADV_API_KEY")
NEWS_KEY = os.getenv("NEWS_API_KEY")

STOCK = "AAPL"
COMPANY_NAME = "APPLE"

STOCK_API_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_KEY}"
NEWS_API_ENDPOINT = (
    f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_KEY}"
)


def send_sms(msg_text):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=msg_text,
        to="+923040000000",
        from_="+19783070637",
    )


def get_news():
    response = requests.get(NEWS_API_ENDPOINT)
    response.raise_for_status()
    articles = response.json()["articles"]
    return articles[:3]


def get_stock_data():
    response = requests.get(STOCK_API_ENDPOINT)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for _, value in data.items()]
    return data_list


stock_data = get_stock_data()
yesterday_closing_price = float(stock_data[0]["4. close"])
before_yesterday_closing_price = float(stock_data[1]["4. close"])

diff = yesterday_closing_price - before_yesterday_closing_price
percentage = round((diff / before_yesterday_closing_price) * 100, 2)

if percentage > 5 or percentage < 5:
    articles = get_news()
    msg_icon = "⬆️" if percentage > 0 else "⬇️"
    msg_text = f"{STOCK}: {msg_icon} {abs(percentage)}%\n\n"
    for article in articles:
        msg_text += f"Headline: {article["title"]}\nBrief: {article["description"]}\n\n"

    send_sms(msg_text)
