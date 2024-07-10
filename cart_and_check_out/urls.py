from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='cart'),
    path('checkout/', check_out, name='checkout'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
     path('wishlist/', wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
]
