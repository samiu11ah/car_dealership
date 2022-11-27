from django.shortcuts import render, redirect
from .models import Car, Inquiry
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
import requests
import json
# Create your views here.

def index(request):
    return render(request, 'base/index.html')


def car_details(request, id):
    return render(request, 'base/car_details.html')

def cars(request):
    context = {}
    context['cars'] = Car.objects.all()
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
                    messages.success(request, f'User created and logged in as {user.username}')
                    return redirect('index')
            except:
                messages.error(request, 'Something went wrong, try again')
                return redirect('register')
        else:
            messages.error(request, 'Passwords not matching, retry')
            return redirect('register')

    return render(request, 'base/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in as {user.username}')
            return redirect('index')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('user_login')
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