import requests
import datetime as dt
import os

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/d20469592a7bae833661910e0fcbe1a5/newWorkoutTracker/sheet1"
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEETY_AUTH = "Basic YXNoOTQ3NjpkYXR0ZWJheW8="


def get_workout_data(exercise):
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY
    }
    params = {
        "query": exercise
    }
    res = requests.post(url=ENDPOINT, json=params, headers=headers)
    res.raise_for_status()
    return res.json()


def log_workout(exercise_data):
    sheety_headers = {
        "Authorization": SHEETY_AUTH
    }
    for exercise in exercise_data:
        sheety_params = {
            "sheet1": {
                "date": dt.datetime.now().date().strftime("%d/%m/%Y"),
                "time": dt.datetime.now().time().strftime("%H:%M:%S"),
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        sheety_res = requests.post(SHEETY_ENDPOINT, headers=sheety_headers, json=sheety_params)
        sheety_res.raise_for_status()
        print(sheety_res.json())


def main():
    user_input = input("Tell me which exercises you did: ")
    if not user_input:
        print("Exercise input cannot be empty. Please try again.")
        return

    workout_data = get_workout_data(user_input)
    if workout_data:
        log_workout(workout_data)
    else:
        print("No workout data found or there was an error.")


if __name__ == "__main__":
    main()
