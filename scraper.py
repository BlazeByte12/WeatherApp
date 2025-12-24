import requests

def scrape_weather(city: str):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        c = data["current_condition"][0]

        current = {
            "temperature": c.get("temp_C"),
            "feels_like": c.get("FeelsLikeC"),
            "humidity": c.get("humidity"),
            "condition": c["weatherDesc"][0]["value"],
            "wind_speed": c.get("windspeedKmph"),
            "wind_direction": c.get("winddir16Point"),
            "pressure": c.get("pressure"),
            "uv_index": c.get("uvIndex"),
            "visibility": c.get("visibility")
        }

        forecast = []
        for day in data["weather"]:
            forecast.append({
                "date": day["date"],
                "min_temp": day["mintempC"],
                "max_temp": day["maxtempC"],
                "avg_temp": day["avgtempC"],
                "condition": day["hourly"][4]["weatherDesc"][0]["value"]
            })

        return {"current": current, "forecast": forecast}

    except Exception as e:
        return {"error": str(e)}
