import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from scraper import scrape_weather

def plot_weather(city: str):
    data = scrape_weather(city)
    if "error" in data:
        return None

    dates = [d["date"] for d in data["forecast"]]
    temps = [int(d["avg_temp"]) for d in data["forecast"]]

    fig, ax = plt.subplots()
    ax.plot(dates, temps, marker="o")
    ax.set_title(f"3-Day Avg Temp – {city}")
    ax.set_ylabel("°C")
    ax.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return base64.b64encode(buf.read()).decode()
