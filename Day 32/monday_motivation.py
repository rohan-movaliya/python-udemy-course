import datetime as dt
import random
import smtplib

MY_EMAIL = "pythonrohan2@gmail.com"
PASSWORD = "123abcd()"

# obtain weekday
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    # choose random quotes
    with open("quotes.txt") as file:
        data = file.readlines()
    quote = random.choice(data)

    # send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rohanmovaliya@gmail.com",
            msg=f"Subject:Hello \n\n{quote}",
        )
