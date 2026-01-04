from django.db import models
from django.conf import settings

class CarpoolBase(models.Model):
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Offer(CarpoolBase):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='offers')
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Offer from {self.driver.email} at {self.departure_time}"

class Request(CarpoolBase):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='requests')

    def __str__(self):
        return f"Request from {self.passenger.email} at {self.departure_time}"
