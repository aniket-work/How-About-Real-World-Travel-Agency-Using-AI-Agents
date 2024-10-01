def get_attractions(location):
    attractions = {
        "London": ["Tower Bridge", "Big Ben", "Buckingham Palace", "London Eye", "British Museum"],
        "Paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral", "Arc de Triomphe"],
        "New York": ["Statue of Liberty", "Central Park", "Empire State Building", "Times Square"]
    }
    city_attractions = attractions.get(location, ["Local Museum", "City Park", "Historical Landmark"])
    selected = random.sample(city_attractions, min(3, len(city_attractions)))
    return f"Top attractions in {location}: {', '.join(selected)}"