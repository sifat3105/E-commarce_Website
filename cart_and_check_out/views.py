from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Wishlist
from Account_Dashboard.models import ShippingAddress
from .context_processors import popup_cart

def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


def view_cart(request):
    # cart = get_object_or_404(Cart, user=request.user)
    # cart_items = CartItem.objects.filter(cart=cart)
    
    return render(request, 'cart/shop_cart.html')

def check_out(request):
    try:
        cart_data = popup_cart(request)
        total_product_price = cart_data['total_product_price']
    except:
        None
    if request.user.is_authenticated:
        shipping_message ='10.00'
        shipping_charge = 10
        address = get_object_or_404(ShippingAddress, user = request.user)
        if address.city.lower() == 'dhaka':
            shipping_message = 'Free Shipping'
            shipping_charge = 00
        
        total_checkout_price = total_product_price+shipping_charge
    return render(request, 'cart/checkout.html',{
        'shipping_message':shipping_message,
        'shipping_charge':shipping_charge,
        'total_checkout_price':total_checkout_price,
        'address':address,
    })

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')



def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
       return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))

def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'cart/wishlist.html', {'wishlist_items': wishlist_items})