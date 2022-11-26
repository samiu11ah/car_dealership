from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    image = models.ImageField(upload_to='cars/')
    make = models.CharField(max_length=100) # tesla, toyota
    model = models.CharField(max_length=100) # corola
    # addtinal column
    model_year = models.CharField(max_length=4, default='1960')

    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    # additional columns
    condition = models.CharField(max_length=100, choices=(('new', 'new'), ('old', 'old')))
    condition_rating = models.CharField(max_length=100, blank=True, null=True, choices=(('10', '10/10'), ('9', '9/10'), ('8', '8/10'), ('7', '7/10'), ('6', '6/10'), ('5', '5/10'), ('4', '4/10'), ('3', '3/10'), ('2', '2/10'), ('1', '1/10')))
    description = models.TextField(blank=True, null=True)
    sold = models.BooleanField(default=False)
    sold_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return f'id: {self.id}, make: {self.make}, model: {self.model}, year: {self.model_year}'

class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=False)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Inquiries"


    def __str__(self):
        return f'{self.email}: {self.message.splitlines()[0]}'
