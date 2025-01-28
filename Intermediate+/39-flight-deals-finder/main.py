import requests
from flight_data import FlightData
from data_manager import DataManager

FLIGHTS_ENDPOINT = "https://test.api.amadeus.com/v1"
SHEETY_ENDPOINT = "https://api.sheety.co/d20469592a7bae833661910e0fcbe1a5/copyOfFlightDealsNew/prices"
sheety_headers = {
    "Authorization": "Basic YXNoOmFzaEA5NDc2"
}

flights_headers = {
    "Authorization": "Bearer mZpZGpXlMp4YcTGh068GzDW5UCIv"
}

data_manager = DataManager(SHEETY_ENDPOINT)
flight_data = FlightData(FLIGHTS_ENDPOINT)
data = data_manager.get_data(headers=sheety_headers)

for city in data:
    print(f"Processing city: {city['city']}")
    airport_data = flight_data.get_iata_code(headers=flights_headers, city=city["city"])
    if airport_data:
        print(f"Found IATA code: {airport_data[0]['iataCode']}")
        city["iataCode"] = airport_data[0]['iataCode']

        update_data = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        data_manager.update_sheets(url=f"{SHEETY_ENDPOINT}/{city['id']}", headers=sheety_headers, params=update_data)
    else:
        print(f"No IATA code found for {city['city']}")

search_params = {
                "originLocationCode": "LON",
                "destinationLocationCode": city,
                "departureDate": result_date.strftime("%Y-%m-%d"),
                "adults": 1,
                "maxPrice": 240
            }

