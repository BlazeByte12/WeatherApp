from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from database import create_database
from routers.auth_router import router as auth_router
from routers.weather_router import router as weather_router
from graph import plot_weather  # koristi funkciju iz graph.py

app = FastAPI(title="Weather App System")

create_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Home ruta
@app.get("/", response_class=HTMLResponse)
def home():
    index_path = os.path.join("frontend", "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

app.include_router(auth_router, prefix="/auth")
app.include_router(weather_router, prefix="/api")

@app.get("/api/weather_graph/{city}")
def weather_graph(city: str):
    try:
        plot_weather(city)  # prikazuje graf
        return {"message": f"Graph displayed for city {city}"}
    except Exception as e:
        return {"error": str(e)}

