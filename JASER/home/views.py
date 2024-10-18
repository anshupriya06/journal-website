from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

# def home_view(request):
#     return HttpResponse("Welcome to the Home Page")

def index(request):
    return render(request, 'home/index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home/index.html')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'home/login.html')
