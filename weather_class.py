from datetime import datetime

class Weather:
    def __init__(self, city: str, temperature: float, condition: str, timestamp: str = None):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.timestamp = timestamp or datetime.now().isoformat()

    def to_dict(self):
        return {
            "city": self.city,
            "temperature": self.temperature,
            "condition": self.condition,
            "timestamp": self.timestamp
        }

    def __str__(self):
        return f"{self.city} | {self.temperature}°C | {self.condition} | {self.timestamp}"

    def is_hot(self, threshold: float = 30.0):
        return self.temperature >= threshold

if __name__ == "__main__":
    w = Weather(city="Sarajevo", temperature=5.5, condition="Cloudy")
    print(w)
    print(w.to_dict())
    print(w.is_hot())