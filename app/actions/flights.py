import random


def search_flights(origin, destination, date):
    airlines = ["Air Canada", "British Airways", "Lufthansa", "Emirates"]
    flight = {
        "airline": random.choice(airlines),
        "flight_number": f"{random.choice(['AC', 'BA', 'LH', 'EK'])}{random.randint(100, 999)}",
        "departure": f"{date} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
        "arrival": f"{date} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
        "price": random.randint(500, 1500)
    }
    return f"Found flight: {flight['airline']} {flight['flight_number']} from {origin} to {destination}, " \
           f"Departure: {flight['departure']}, Arrival: {flight['arrival']}, Price: ${flight['price']}"