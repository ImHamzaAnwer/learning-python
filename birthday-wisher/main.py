import random
import pandas as pd
import datetime as dt
import os
import smtplib

recipients = pd.read_csv("birthday-wisher/birthdays.csv").to_dict(orient="records")

SENDER_EMAIL = "yoyo@yoyo.com"
today = dt.datetime.now()
template_paths = os.listdir("birthday-wisher/letter_templates")


def send_mail(content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password="abba jabba")
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Habby Birthday\n\n{content}",
        )

for person in recipients:
    random_template_path = (
        f"birthday-wisher/letter_templates/{random.choice(template_paths)}"
    )
    if person["month"] == today.month and person["day"] == today.day:
        with open(random_template_path) as template:
            content = template.read()
            content = content.replace("[NAME]", person["name"])
            send_mail(content)
