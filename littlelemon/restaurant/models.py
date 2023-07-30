from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators = [MinValueValidator(0)])
    inventory = models.PositiveSmallIntegerField(default=0)

    def __str__(self)-> str:
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(default=0)
    booking_date = models.DateTimeField()

    def __str__(self)-> str:
        return self.name