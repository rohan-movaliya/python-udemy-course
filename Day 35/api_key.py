# This program is incomplete.
# Because in this program using API doesn't worked.
import requests

API_KEY = " "

parameters = {
    "lat": 23.0333,
    "lon": 72.6167,
    "exclude": "current,hourly",
    "appid": API_KEY,
}


response = requests.get(
    "https://api.openweathermap.org/data/3.0/onecall", params=parameters
)
response.raise_for_status()
data = response.json()
print(data)
