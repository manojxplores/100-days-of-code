import requests
import datetime

FLIGHTS_ENDPOINT = "https://test.api.amadeus.com/v2"

flights_headers = {
    "Authorization": "Bearer ACCESS_TOKEN_HERE"
}


class FlightSearch:

    def get_flight_offers(self, dep_date, origin, destination, max_price):
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": dep_date,
            "adults": 1,
            "max": 1,
            "maxPrice": max_price
        }

        res = requests.get(f"{FLIGHTS_ENDPOINT}/shopping/flight-offers", headers=flights_headers, params=params)
        res.raise_for_status()
        return res.json()
