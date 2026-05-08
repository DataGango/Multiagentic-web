from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Hotel, Booking
import json

def index(request):
    return render(request, 'index.html')

def test_results(request):
    return render(request, 'test_results.html')

@csrf_exempt
def check_availability(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hotel_name = data.get('hotel', 'Unknown')
        try:
            hotel = Hotel.objects.get(name=hotel_name)
            return JsonResponse({"status": "success", "message": f"{hotel.name} currently has {hotel.available_rooms} luxury suites available."})
        except Hotel.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Hotel not found in database."})
    return JsonResponse({"error": "POST required"}, status=400)

@csrf_exempt
def book_room(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hotel_name = data.get('hotel', 'Unknown')
        try:
            hotel = Hotel.objects.get(name=hotel_name)
            if hotel.available_rooms > 0:
                hotel.available_rooms -= 1
                hotel.save()
                Booking.objects.create(hotel=hotel, guest_name="VIP Guest")
                return JsonResponse({"status": "success", "message": f"Successfully booked a suite at {hotel.name}! {hotel.available_rooms} rooms left."})
            else:
                return JsonResponse({"status": "error", "message": f"Sorry, {hotel.name} is fully booked!"})
        except Hotel.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Hotel not found in database."})
    return JsonResponse({"error": "POST required"}, status=400)

@csrf_exempt
def cancel_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hotel_name = data.get('hotel', 'Unknown')
        try:
            hotel = Hotel.objects.get(name=hotel_name)
            booking = Booking.objects.filter(hotel=hotel, is_active=True).first()
            if booking:
                booking.is_active = False
                booking.save()
                hotel.available_rooms += 1
                hotel.save()
                return JsonResponse({"status": "success", "message": f"Your booking at {hotel.name} has been cancelled. Room added back to availability."})
            else:
                return JsonResponse({"status": "error", "message": f"No active bookings found for you at {hotel.name}."})
        except Hotel.DoesNotExist:
             return JsonResponse({"status": "error", "message": "Hotel not found in database."})
    return JsonResponse({"error": "POST required"}, status=400)

@csrf_exempt
def get_pricing(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hotel_name = data.get('hotel', 'Unknown')
        try:
            hotel = Hotel.objects.get(name=hotel_name)
            return JsonResponse({"status": "success", "message": f"Current pricing for {hotel.name} starts at ${hotel.base_price}/night."})
        except Hotel.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Hotel not found in database."})
    return JsonResponse({"error": "POST required"}, status=400)

@csrf_exempt
def contact_hotel(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        hotel_name = data.get('hotel', 'Unknown')
        return JsonResponse({"status": "success", "message": f"Message delivered to the front desk concierge at {hotel_name}."})
    return JsonResponse({"error": "POST required"}, status=400)
