from .models import Cart, CartItem
from django.shortcuts import get_object_or_404, redirect, render

def popup_cart(request):
    if request.user.is_authenticated:
        try:
            cart = get_object_or_404(Cart, user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            total_cart_item = len(cart_items)
            total = 00
            if cart_items:
                for item in cart_items:
                    if not item.subtotal:
                        subtotal = 00
                    else:
                        subtotal = item.subtotal
                    total+=subtotal
        except:
            None
    return locals()
    # return {'cart_items':cart_items,'total_product_price':total, 'total_cart_item':total_cart_item}
