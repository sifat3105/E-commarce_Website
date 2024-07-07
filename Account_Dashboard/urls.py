from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='account' ),
    path('billing_update/', billing_update, name='billing_update'),
    path('shipping_update/', shipping_update, name='shipping_update'),
]
