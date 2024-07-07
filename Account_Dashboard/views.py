from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.


def dashboard_view(request):
    try:
        Billing_Address = BillingAddress.objects.get(user=request.user)
    except BillingAddress.DoesNotExist:
        Billing_Address = BillingAddress(
            user=request.user,
            street_address='House #12, Road #7, Dhanmondi',
            city='Dhaka',
            state='Dhaka Division',
            postal_code='1205',
            country='Bangladesh',
            number='+880-1234-567890'
        )

    try:
        Shipping_Address = ShippingAddress.objects.get(user=request.user)
    except ShippingAddress.DoesNotExist:
        Shipping_Address = ShippingAddress(
            street_address='House #12, Road #7, Dhanmondi',
            city='Dhaka',
            state='Dhaka Division',
            postal_code='1205',
            country='Bangladesh',
            number='+880-1234-567890'

        )
    return render(request,'account/account_dashboard.html',{
            'Billing_Address':Billing_Address,
            'Shipping_Address':Shipping_Address,
        })



def billing_update(request):
    if request.method == 'POST':
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        number = request.POST.get('phone')
        
        
        data, created = BillingAddress.objects.get_or_create(user=request.user)
        data.street_address = street_address
        data.city = city
        data.state=  state
        data.postal_code = postal_code
        data.country = country
        data.number = number
        data.save()
        messages.success(request, 'Billing Address Update Successfully')
        return redirect('account')
    return render(request, 'Home/home.html')


def shipping_update(request):
    if request.method == 'POST':
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        number = request.POST.get('phone')
        
        data, created = ShippingAddress.objects.get_or_create(user = request.user)
        data.street_address = street_address
        data.city = city
        data.state=  state
        data.postal_code = postal_code
        data.country = country
        data.number = number
        data.save()
        
        messages.success(request, 'Shipping Address Update Successfully')
        return redirect('account')
        
    return render(request, 'Home/home.html')