import requests
from flight_data import FlightData


class DataManager:
    def __init__(self, url):
        self.url = url

    def get_data(self, headers):
        res = requests.get(url=self.url, headers=headers)
        res.raise_for_status()
        return res.json()['prices']

    def update_sheets(self, url, headers, params):
        response = requests.put(url=url, headers=headers, json=params)
        response.raise_for_status()
        print(response.status_code)
