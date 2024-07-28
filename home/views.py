from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from Product.models import Product, Banner
# Create your views here.


def home_view(request):
    banners = Banner.objects.all()
    ban_len = len(banners)-1
    banner = banners[ban_len]
    return render(request,'Home/home.html',locals())


def all_product_viow(request):
    
    return render(request, 'Home/all_product.html')


def quick_view(request, uuid):
    product = get_object_or_404(Product, uuid = uuid)
    return render(request,'Home/home.html',{'quick_view_product':product}) 