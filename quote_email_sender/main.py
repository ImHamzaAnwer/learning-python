import smtplib
import random
import datetime as dt

EMAIL = "haha@hehe.com"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 6:
    with open("quote_email_sender/quotes.txt") as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password="hehehe")
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:SUNDAY MOTIVATION \n\n {random_quote}".encode("utf8"),
        )
