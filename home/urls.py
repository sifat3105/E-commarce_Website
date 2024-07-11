from django.urls import path
from .views import home_view, all_product_viow

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', all_product_viow, name='all_product'),
    
]
