import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

params = {
    "lat": 9.453040,
    "lon": 77.793922,
    "cnt": 4,
    "appid": API_KEY
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
res.raise_for_status()
data = res.json()

# create an instance from the Client class
will_rain = False
for hour_data in data["list"]:
    if hour_data["weather"][0]["id"] < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!☂️",
        from_="+15074422434",
        to="+91xxxxxxxx",
    )
