import requests

PRICES_ENDPOINT = "https://api.sheety.co/d20469592a7bae833661910e0fcbe1a5/copyOfFlightDealsNew/prices"
USERS_ENDPOINT = "https://api.sheety.co/d20469592a7bae833661910e0fcbe1a5/copyOfFlightDealsNew/users"
sheety_headers = {
    "Authorization": "Basic YXNoOmFzaEA5NDc2"
}


class DataManager:
    def get_data(self):
        res = requests.get(url=PRICES_ENDPOINT, headers=sheety_headers)
        res.raise_for_status()
        return res.json()['prices']

    def get_customer_emails(self):
        user_res = requests.get(url=USERS_ENDPOINT, headers=sheety_headers)
        user_res.raise_for_status()
        return user_res.json()

    def update_sheets(self, row_id, params):
        response = requests.put(url=f"{PRICES_ENDPOINT}/{row_id}", headers=sheety_headers, json=params)
        response.raise_for_status()
        print(response.status_code)
