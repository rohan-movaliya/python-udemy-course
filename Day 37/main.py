import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "mygraphpython"

# Create your user account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Course Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}
headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Get the graph!
# Using this URL : https://pixe.la/v1/users/<USERNAME>/graphs/<GRAPH_ID>


# Post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours you learn python: "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


# Update a Pixel
update_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)
new_pixel_data = {"quantity": "10.10"}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# Delete a Pixel
delete_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
