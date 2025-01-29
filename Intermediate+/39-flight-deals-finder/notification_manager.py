from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, price, origin, dest, start, end):
        message = self.client.messages.create(
            body=f"Low price alert! Only €{price} to fly from {origin} to {dest}, on {start} until {end}",
            from_="+15074422434",
            to="+919392891224",
        )
        print(message.body)