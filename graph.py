import sqlite3
from database import get_db_connection
import matplotlib.pyplot as plt

def plot_weather(city: str):

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT temperature, timestamp FROM weather_logs WHERE city = ? ORDER BY timestamp ASC",
            (city,)
        )
        rows = cursor.fetchall()

        if not rows:
            print(f"Nema podataka za grad: {city}")
            return

        temperatures = [row["temperature"] for row in rows]
        timestamps = [row["timestamp"] for row in rows]

        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='blue')
        plt.title(f"Temperature over time in {city}")
        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    finally:
        conn.close()


if __name__ == "__main__":
    grad = input("Unesi ime grada za graf: ")
    plot_weather(grad)
