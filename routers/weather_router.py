import datetime
from fastapi import APIRouter, Depends, HTTPException
from models.weather import WeatherRequest
from auth.security import api_key_header
from database import get_db_connection
from api import get_weather
from scraper import scrape_weather

router = APIRouter()

@router.post("/weather")
def fetch_weather(req: WeatherRequest, api_key: str = Depends(api_key_header)):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM users WHERE api_key = ?", (api_key,))
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=403, detail="Invalid API key")

        weather = get_weather(req.city)
        if "error" in weather:
            raise HTTPException(status_code=404, detail=weather["error"])

        cursor.execute(
            "INSERT INTO weather_logs (user_id, city, temperature, condition, timestamp) VALUES (?, ?, ?, ?, ?)",
            (user["id"], req.city, weather["temperature"], weather["condition"], datetime.datetime.now().isoformat())
        )
        conn.commit()
        return weather
    finally:
        conn.close()


@router.get("/scrape/{city}")
def scrape(city: str):
    result = scrape_weather(city)
    return {"result": result}
