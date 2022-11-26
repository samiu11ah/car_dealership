from django.contrib import admin
from .models import Car, Inquiry
# Register your models here.
admin.site.site_header = "Car Dealership"
admin.site.index_title = 'Admin: Dealership Area'


admin.site.register(Car)
admin.site.register(Inquiry)