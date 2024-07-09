from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from Product.utils import convert_to_16_9
from Product.models import Product
# Create your views here.


def home_view(request):
    return render(request,'Home/home.html',locals())


def all_product_viow(request):
    return render(request, 'Home/all_product.html')