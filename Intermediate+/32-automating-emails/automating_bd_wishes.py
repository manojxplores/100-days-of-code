import datetime as dt
import pandas as pd
import smtplib

email = "ash11256@gmail.com"
password = "your_password_here"

df = pd.read_csv("birthdays.csv")

for index, row in df.iterrows():
    now = dt.datetime.now()
    if row["month"] == now.month and row["day"] == now.day:
        with open("template.txt") as file:
            content = file.read()
            message = content.replace("{NAME}", row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject: Happy Birthday {row['name']}\n\n{message}"
            )

