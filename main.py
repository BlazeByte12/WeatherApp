from fastapi import FastAPI
from routers.weather_router import router

app = FastAPI()

app.include_router(router)
