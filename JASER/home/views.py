from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

# def home_view(request):
#     return HttpResponse("Welcome to the Home Page")

def index(request):
    return render(request, 'home/index.html')

