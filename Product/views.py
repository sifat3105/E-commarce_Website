from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, SubCategory, Reviews
from .forms import BannerForm, Banner2Form, DealForm, FeaturedBrandForm, ProductForm
from django.contrib import messages





def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or another page
    else:
        form = ProductForm()
    return render(request, 'product/Create Views/create_product.html', {'form': form})


def product_view(request):
    products = Product.objects.all()
    return render(request, 'product/product_view.html')



def right_product_view(request , uuid):
    product = get_object_or_404(Product, uuid = uuid)
    reviews = Reviews.objects.filter(product=product)
    ratings = 0
    try:
        num_review = len(reviews)
        rate = 0
        star_1=0
        star_2=0
        star_3=0
        star_4=0
        star_5=0
        star_slider_1=0
        star_slider_2=0
        star_slider_3=0
        star_slider_4=0
        star_slider_5=0
        show_rating = 0
        for i in reviews:
            rate += i.rating

        show_rating = rate/num_review
        ratings =show_rating/20
        if ratings not in {5, 4, 3, 2, 1}:
            ratings = round(ratings,1)
        for i in reviews:
            if i.rating == 20:
                star_1 +=1
            elif i.rating == 40:
                star_2 +=1
            elif i.rating == 60:
                star_3 +=1
            elif i.rating == 80:
                star_4 +=1
            elif i.rating == 100:
                star_5+=1
        if num_review > 0:
            star_slider_1 = round((star_1 / num_review) * 100)
            star_slider_2 = round((star_2 / num_review) * 100)
            star_slider_3 = round((star_3 / num_review) * 100)
            star_slider_4 = round((star_4 / num_review) * 100)
            star_slider_5 = round((star_5 / num_review) * 100)
        else:
            star_slider_1 = 0
            star_slider_2 = 0
            star_slider_3 = 0
            star_slider_4 = 0
            star_slider_5 = 0
    except:
        None

    
    product.num_reviews = num_review
    if ratings:
        product.rating = ratings
        product.show_rating= show_rating
        product.save()

    if request.method == 'POST':
        comment = request.POST.get("comment")
        rating = request.POST.get('rating')
        if rating:
            rating = rating
        else:
            rating = 0
        if request.user.is_authenticated:
            name =f"{ request.user.first_name} { request.user.last_name}"
            print(name, rating)
            product = get_object_or_404(Product, uuid=uuid)
            Reviews.objects.create(comment=comment, rating=rating, name=name, product=product, )
            messages.success(request, 'Your review has been submitted.')
            
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'You must be logged in to submit a review.')
            return redirect('login_registration')


    return render(request, 'product/full_product_view.html', {
        'product':product,
        'reviews':reviews,
        'star_slider_1':star_slider_1,
        'star_slider_2':star_slider_2,
        'star_slider_3':star_slider_3,
        'star_slider_4':star_slider_4,
        'star_slider_5':star_slider_5,
        
        })





def banner_create_view(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            print ('is it okay')
            form.save()
            return redirect('success') 
        else:
            print('it  not okay')
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


# views.py
from django.shortcuts import render, redirect

def submit_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            print(f"Received rating: {rating}")
            
    return render(request, 'template.html')
