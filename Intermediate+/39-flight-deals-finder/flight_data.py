import requests
import os

# API_KEY = os.environ.get("API_KEY")
# API_SECRET = os.environ.get("API_SECRET")
# headers = {
#     "content-type": "application/x-www-form-urlencoded"
# }
#
# params = {
#     "grant_type": "client_credentials",
#     "client_id": API_KEY,
#     "client_secret": API_SECRET
# }
#
# res = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=params)
# res.raise_for_status()
# print(res.json())

FLIGHTS_ENDPOINT = "https://test.api.amadeus.com/v1"
flights_headers = {
    "Authorization": "Bearer ACCESS_TOKEN_HERE"
}


class FlightData:
    # This class is responsible for structuring the flight data.
    def get_iata_code(self, city):
        params = {
            "subType": "CITY",
            "keyword": city
        }

        res = requests.get(f"{FLIGHTS_ENDPOINT}/reference-data/locations", headers=flights_headers, params=params)
        res.raise_for_status()
        data = res.json()["data"]
        return data


