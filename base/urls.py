from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cars/', views.cars, name='cars'),
    path('my_rides/', views.my_rides, name='my_rides'),
    path('book_ride/<str:car_id>', views.book_ride, name='book_ride'),

    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('enquiry/', views.inquiry, name='inquiry'),
]
