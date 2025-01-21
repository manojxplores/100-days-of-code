import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "jkK02E40FAhvsjhjv9sp"
USERNAME = "ash11256"

# Create a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# res = requests.post(url=pixela_endpoint, json=user_params)
# res.raise_for_status()
# print(res.text)


# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "sora"
}

# graph_res = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_res.text)

# Post a pixel
now = datetime.now()
formatted_date = now.strftime("%Y%m%d")

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
post_pixel_params = {
    "date": formatted_date,
    "quantity": "1"
}
res = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(res.text)

# Update a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"
update_pixel_params = {
    "quantity": "4"
}
# res = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(res.text)

# Delete a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20250120"
# res = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(res.text)
