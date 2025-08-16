import requests
import os
from datetime import datetime
from dotenv import load_dotenv


# Load Environment Variables
load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("BEARER_TOKEN")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

# User Configuration
USER_PROFILE = {
    "gender": "male",  # Update to your gender
    "weight_kg": 70,  # Replace with your weight
    "height_cm": 175,  # Replace with your height
    "age": 25,  # Replace with your age
}

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

BEARER_HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_exercises(query: str):
    """Send user exercise query to Nutritionix API and return parsed results."""
    params = {**USER_PROFILE, "query": query}
    try:
        response = requests.post(NUTRITIONIX_ENDPOINT, json=params, headers=HEADERS)
        response.raise_for_status()
        result = response.json()
        return result.get("exercises", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching exercises: {e}")
        return []


def log_to_sheet(exercise: dict):
    """Log a single exercise record to Sheety API."""
    now = datetime.now()
    sheet_inputs = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    try:
        response = requests.post(
            SHEET_ENDPOINT, json=sheet_inputs, headers=BEARER_HEADERS
        )
        response.raise_for_status()
        print(
            f"✅ Logged: {exercise['name'].title()} "
            f"({exercise['duration_min']} min, {exercise['nf_calories']} cal)"
        )
    except requests.exceptions.RequestException as e:
        print(f"❌ Error logging to sheet: {e}")


# Main Function
def main():
    query = input("Tell me which exercises you did: ").strip()
    if not query:
        print("⚠️ No input provided. Exiting.")
        return

    exercises = get_exercises(query)
    if not exercises:
        print("⚠️ No exercises found. Check your query or API credentials.")
        return

    for ex in exercises:
        log_to_sheet(ex)


# Run Program
if __name__ == "__main__":
    main()
