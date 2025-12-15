import requests
from bs4 import BeautifulSoup

def scrape_weather(city: str):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return response.text

