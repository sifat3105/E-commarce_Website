from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.


def home_view(request):
   
    return render(request,'Home/home.html')
