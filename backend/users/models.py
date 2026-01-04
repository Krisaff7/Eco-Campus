from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='passenger')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    default_start_point = models.CharField(max_length=255, null=True, blank=True)
    default_arrival_time = models.TimeField(null=True, blank=True)
    default_departure_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.email}"

class Vehicle(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vehicle')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} - {self.owner.email}"
