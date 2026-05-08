import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from bookings.models import Hotel

hotels_data = [
    {"name": "Hilton Maldives Resort", "location": "Maldives", "base_price": 500.00, "total_rooms": 20, "available_rooms": 15},
    {"name": "Marriott Tokyo Downtown", "location": "Tokyo", "base_price": 300.00, "total_rooms": 100, "available_rooms": 40},
    {"name": "The Ritz Paris", "location": "Paris", "base_price": 800.00, "total_rooms": 30, "available_rooms": 5},
    {"name": "Four Seasons Bali", "location": "Bali", "base_price": 400.00, "total_rooms": 50, "available_rooms": 50},
]

for data in hotels_data:
    hotel, created = Hotel.objects.get_or_create(name=data["name"], defaults=data)
    if not created:
        for key, value in data.items():
            setattr(hotel, key, value)
        hotel.save()

print("Database populated successfully with hotels and availabilities!")
