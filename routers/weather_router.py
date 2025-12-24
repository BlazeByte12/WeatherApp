from fastapi import APIRouter, HTTPException
from scraper import scrape_weather
from graph import plot_weather

router = APIRouter(prefix="/api")


@router.get("/weather/current")
def current_weather(city: str):
    data = scrape_weather(city)
    if "error" in data:
        raise HTTPException(status_code=404, detail="Weather not found")
    return data["current"]


@router.get("/weather/forecast")
def forecast(city: str):
    data = scrape_weather(city)
    if "error" in data:
        raise HTTPException(status_code=404, detail="Forecast not found")
    return data["forecast"]


@router.get("/weather/history")
def history(city: str):
    graph_base64 = plot_weather(city)
    if not graph_base64:
        raise HTTPException(status_code=404, detail="History not found")
    return {"graph": f"data:image/png;base64,{graph_base64}"}
