import requests
import datetime

class FlightSearch:

    def get_flight_offers(self, headers, origin, destination, max_price):
        start_date = datetime.datetime.now()
        delta = datetime.timedelta(days=10)
        end_date = start_date + delta

        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": start_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "maxPrice": max_price
        }

        for delta in range((end_date - start_date).days + 1):
            result_date = start_date + datetime.timedelta(days=delta)

        res = requests.get(f"{self.url}/shopping/flight-offers", headers=headers, params=params)
        res.raise_for_status()
        return res.json()


