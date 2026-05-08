from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, default=250.00)
    total_rooms = models.IntegerField(default=50)
    available_rooms = models.IntegerField(default=50)

    def __str__(self):
        return self.name

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, default='VIP Guest')
    booking_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.guest_name} at {self.hotel.name}"
