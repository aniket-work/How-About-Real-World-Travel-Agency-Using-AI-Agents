import random

def find_hotels(location, check_in, check_out, guests):
    hotels = ["Hilton", "Marriott", "Sheraton", "Holiday Inn"]
    hotel = {
        "name": random.choice(hotels),
        "rating": random.randint(3, 5),
        "price": random.randint(100, 300),
        "amenities": random.sample(["WiFi", "Pool", "Gym", "Restaurant", "Bar"], k=3)
    }
    return f"Found hotel: {hotel['name']} ({hotel['rating']} stars) in {location} from {check_in} to {check_out}, " \
           f"Price: ${hotel['price']} per night, Amenities: {', '.join(hotel['amenities'])}"
