import requests
from datetime import datetime

# ISS API(Application Programming Interface)
featched_iss = requests.get("http://api.open-notify.org/iss-now.json")
featched_iss.raise_for_status()

print(featched_iss.status_code)
data = featched_iss.json()
print(data)

message = data["message"]
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
timestamp = data["timestamp"]
print(message)
print(longitude)
print(latitude)
print(timestamp)


# QUOTES API
quotes = requests.get("https://api.kanye.rest")
quotes.raise_for_status()
quotes_data = quotes.json()
print(quotes_data["quote"])

# SUNRAISE AND SUNSET TIME API(with parameters)
parameters = {"lat": 20.5937, "lng": 78.9629, "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


now_time = datetime.now()
print(now_time.hour)
