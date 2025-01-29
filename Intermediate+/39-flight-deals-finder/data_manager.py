import requests

SHEETY_ENDPOINT = "https://api.sheety.co/d20469592a7bae833661910e0fcbe1a5/copyOfFlightDealsNew/prices"
sheety_headers = {
    "Authorization": "Basic AUTH_TOKEN_HERE"
}


class DataManager:
    def get_data(self):
        res = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        res.raise_for_status()
        return res.json()['prices']

    def update_sheets(self, row_id, params):
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", headers=sheety_headers, json=params)
        response.raise_for_status()
        print(response.status_code)
