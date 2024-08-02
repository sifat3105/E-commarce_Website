from django.contrib import admin
from .models import  Cart, CartItem, Wishlist,OrderConfirm, OrderProduct

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(OrderConfirm)
admin.site.register(OrderProduct)
