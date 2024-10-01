import random

def recommend_restaurants(location, cuisine=None):
    restaurants = [
        {"name": "The Local Spot", "cuisine": "Local", "price": "$$"},
        {"name": "Gourmet Delight", "cuisine": "French", "price": "$$$"},
        {"name": "Sushi Heaven", "cuisine": "Japanese", "price": "$$"},
        {"name": "Mama's Kitchen", "cuisine": "Italian", "price": "$$"}
    ]
    selected = random.sample(restaurants, 2)
    return f"Recommended restaurants in {location}: " + ", ".join([f"{r['name']} ({r['cuisine']} cuisine, {r['price']})" for r in selected])
