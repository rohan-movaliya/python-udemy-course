import requests
from datetime import datetime


APP_ID = ""
API_KEY = ""
GENDER = "Male"
WEIGHT_KG = "68"
HEIGHT_CM = "180"
AGE = "19"
USERNAME = ""
PASSWORD = ""
TOKEN = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6393dda18c202b4d518db11e46196f8b/rohan/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # No Auth
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(USERNAME, PASSWORD)
    # )

    bearer_headers = {"Authorization": f"Bearer {TOKEN}"}
    sheet_response = requests.post(
        sheet_endpoint, json=sheet_inputs, headers=bearer_headers
    )

print(sheet_response.text)
