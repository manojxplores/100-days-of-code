import datetime
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()
notification_manager = NotificationManager()
data = data_manager.get_data()

# for city in data:
#     print(f"Processing city: {city['city']}")
#     airport_data = flight_data.get_iata_code(city=city["city"])
#     if airport_data:
#         print(f"Found IATA code: {airport_data[0]['iataCode']}")
#         city["iataCode"] = airport_data[0]['iataCode']
#
#         update_data = {
#             "price": {
#                 "iataCode": city["iataCode"]
#             }
#         }
#         data_manager.update_sheets(row_id=city['id'], params=update_data)
#     else:
#         print(f"No IATA code found for {city['city']}")


start_date = datetime.datetime.now()
delta = datetime.timedelta(days=180)
end_date = start_date + delta
for delta in range((end_date - start_date).days + 1):
    result_date = start_date + datetime.timedelta(days=delta)
    for city in data:
        print(f"Searching for cheap flights to {city['city']} on {result_date}")
        search_results = flight_search.get_flight_offers(origin="LON", dep_date=result_date.date().strftime("%Y-%m-%d"),
                                                         destination=city['iataCode'], max_price=city['lowestPrice'])
        if search_results["meta"]["count"] != 0:
            price = search_results['data'][0]['price']["total"]
            last_ticketing_date = search_results['data'][0]['lastTicketingDateTime']
            notification_manager.send_message(price=price, start=result_date.date(), end=last_ticketing_date,
                                              origin="LON", dest=city['iataCode'])


