from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import Car, Inquiry, RideRecord
import requests
import json
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def my_rides(request):
    context = {}
    context['my_rides'] = RideRecord.objects.filter(user=request.user)
    return render(request, 'base/my_rides.html', context)

@login_required
def book_ride(request, car_id):
    context = {}
    car = Car.objects.get(id=car_id)

    if request.method == "POST":
        ride_datetime = request.POST.get('ride_date')
        # ride_time = request.POST.get('ride_time')
        ride_spot = request.POST.get('ride_spot')
        # 2022-11-30 12:12

        ride_record = RideRecord(car=car, user=request.user, ride_datetime=ride_datetime, spot=ride_spot)
        ride_record.save()
        messages.success(request, 'Booked ride')
        print(ride_datetime)
        # return redirect('my_rides')

    context['car'] = car
    return render(request, 'base/book_ride.html', context)

def cars(request):
    context = {}

    context['cars'] = Car.objects.all()
    # context['cars'] = RideRecord.objects.filter(user=request.user)
    return render(request, 'base/cars.html', context)

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User(first_name=first_name, last_name=last_name, username=username, email=email)
                user.set_password(password1)
                user.save()
                
                u = authenticate(username=username, password=password1)
                if u is not None:
                    login(request, u)
                    if 'next' in request.GET:
                        messages.success(request, f'User created and logged in as {u.username}, please proceed with booking car ride.')
                        return redirect(request.GET.get('next'))
                    else:
                        messages.success(request, f'User created and logged in as {user.username}')
                        return redirect('index')
                        
            except:
                messages.error(request, 'Something went wrong, try again')
                return redirect('register')
        else:
            messages.error(request, 'Passwords not matching, retry')
            return redirect('register')

    if 'next' in request.GET:
        messages.success(request, f'After creating account, You will be redirected to booking car ride page.')

    return render(request, 'base/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                messages.success(request, f'Logged in as {user.username}, please proceed with booking car ride.')
                return redirect(request.GET.get('next'))
            else:
                messages.success(request, f'Logged in as {user.username}')
                return redirect('index')
        else:
            messages.error(request, 'Something went wrong')
            if 'next' in request.GET:
                next_url = request.GET.get('next')
                return redirect(f'/user_login/?next={next_url}')
            return redirect('user_login')


    if 'next' in request.GET:
        messages.success(request, f'After login, You will be redirected to booking car ride page.')

    return render(request, 'base/user_login.html')

def user_logout(request):
    logout(request)
    messages.warning(request, 'Logged out.')
    return redirect('user_login')

def inquiry(request):
    context = {}
    if request.method == "POST":
        recap_res = request.POST.get('g-recaptcha-response')
        recap_data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recap_res
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recap_data)
        response = json.loads(r.text)

        recap_verified = response['success']

        if recap_verified:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            enq = Inquiry(first_name=first_name, last_name=last_name, email=email, message=message)
            enq.save()
            messages.success(request, 'Your message has be sent')
        else:
            messages.warning(request, 'Please fill reCaptcha')
        
        return redirect('inquiry')


    context['RECAPTCHA_SITE_KEY'] = settings.RECAPTCHA_SITE_KEY

    return render(request, 'base/inquiry.html', context)