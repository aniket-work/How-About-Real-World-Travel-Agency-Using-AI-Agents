import random
from datetime import datetime, timedelta


def get_weather(location, date):
    conditions = ["Sunny", "Partly cloudy", "Cloudy", "Rainy", "Stormy"]
    temp = random.randint(15, 30)
    condition = random.choice(conditions)
    return f"The weather in {location} on {date} is forecasted to be {condition} with a temperature of {temp}°C."

