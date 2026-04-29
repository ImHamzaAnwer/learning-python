from smtplib import SMTP
import requests
from bs4 import BeautifulSoup


def send_email(product_title):
    connection = SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("email", "password")
    connection.sendmail(
        from_addr="email",
        to_addrs="email",
        msg=f"Subject: Amazon Price Alert! \n\n The day has come to buy {product_title}".encode(
            "utf-8"
        ),
    )


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

url = "https://www.amazon.com/Lenovo-Legion-Tower-AI-Powered-Processor/dp/B0F5YNX43T"

res = requests.get(url, headers=header)
res.raise_for_status()
page_content = res.content

soup = BeautifulSoup(page_content, "html.parser")

price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("PKR")[1]
price_without_comma = float(price_without_currency.replace(",", ""))


if price_without_comma < 660000:
    title = soup.find(id="productTitle").get_text().strip()
    send_email(title)
