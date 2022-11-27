from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cars/', views.cars, name='cars'),
    path('car_details/<str:id>', views.car_details, name='car_details'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('inquiry/', views.inquiry, name='inquiry'),
]
