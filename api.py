import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY_HERE"  # upiši svoj ključ

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
