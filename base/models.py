from django.db import models

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(default=0.0, max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return f'make: {self.make}, model: {self.model}'
