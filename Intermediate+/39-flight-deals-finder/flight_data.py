import requests

# API_KEY = "{}"
# API_SECRET = "{}"g
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


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, url):
        self.url = url

    def get_iata_code(self, headers, city):
        params = {
            "subType": "CITY",
            "keyword": city
        }

        res = requests.get(f"{self.url}/reference-data/locations", headers=headers, params=params)
        res.raise_for_status()
        data = res.json()["data"]
        return data


