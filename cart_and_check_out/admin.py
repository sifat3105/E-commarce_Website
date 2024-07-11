from django.contrib import admin
from .models import  Cart, CartItem, Wishlist

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
