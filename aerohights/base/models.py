from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date/time when a new instance is created
    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date/time when a new instance is created
    def __str__(self):
        return self.name

class Booking(models.Model):
    BOOKING_TYPES = [
        ('Umrah', 'Umrah'),
        ('Hajj', 'Hajj'),
        ('Visit', 'Visit'),
        ('Restaurant', 'Restaurant'),
        ('Other', 'Other'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPES)
    date_of_booking = models.DateField()
    destination = models.CharField(max_length=80)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.PositiveIntegerField(default=1, help_text="Duration in days (for bookings like Umrah, Hajj, Visit)")
    creation_date = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date/time when a new instance is created
    def __str__(self):
        return f"{self.get_booking_type_display()} Booking for {self.client.name}"
