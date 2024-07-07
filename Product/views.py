from django.shortcuts import render, redirect
from .models import Product, Category, SubCategory
from .utils import convert_to_16_9
from .forms import BannerForm, Banner2Form, DealForm, FeaturedBrandForm, ProductForm
from django.contrib import messages





def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another page
    else:
        form = ProductForm()
    return render(request, 'product/Create Views/create_product.html', {'form': form})


def product_view(request):
    products = Product.objects.all()
    return render(request, 'product/product_view.html')



def right_product_view(request , uuid):
    product = Product.objects.get(uuid = uuid)

    return render(request, 'product/right_product_view.html', {'product':product})





def banner_create_view(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another page
    else:
        form = BannerForm()
    return render(request, 'product/Create Views/create_banner.html', {'form': form})

def banner2_create_view(request):
    if request.method == 'POST':
        form = Banner2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        messages.warning(request, 'not work')
        form = Banner2Form()
    return render(request, 'product/Create Views/create_banner2.html', {'form': form})

def deal_create_view(request):
    if request.method == 'POST':
        form = DealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DealForm()
    return render(request, 'product/Create Views/create_deal.html', {'form': form})

def featured_brand_create_view(request):
    if request.method == 'POST':
        form = FeaturedBrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FeaturedBrandForm()
    return render(request, 'product/Create Views/create_featured_brand.html', {'form': form})

def success_view(request):
    return render(request, 'product/Create Views/success.html')


def creation_dashboard_view(request):
    return render(request, 'product/creation_dashboard.html')