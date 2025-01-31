from twilio.rest import Client
import os
import smtplib

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
EMAIL = "test@gmail.com"
PASSWORD = "YOUR_PASSWORD_HERE"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, price, origin, dest, start, end):
        message = self.client.messages.create(
            body=f"Low price alert! Only €{price} to fly from {origin} to {dest}, on {start}",
            from_="+15074422434",
            to="+919392891224",
        )
        print(message.body)

    def send_email(self, price, origin, dest, start, user_email):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=user_email,
                msg=f"Subject: Flight Club!!\n\nLow price alert! Only €{price} to fly from {origin} to {dest}, on {start}"
            )
        print(f"Email sent to {user_email}")

