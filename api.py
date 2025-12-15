import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "ECF57DAEA599C91AF5A2489DA3D16DCC"

def get_weather(city: str):
    city = city.replace(" ", "")
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()
        if response.status_code != 200 or "main" not in data:
            return {"error": f"Grad '{city}' nije pronađen."}
        return {"city": data["name"], "temperature": data["main"]["temp"], "condition": data["weather"][0]["description"]}
    except requests.RequestException:
        return {"error": "Greška prilikom poziva API-ja."}
