from django.contrib import admin
from .models import BillingAddress, ShippingAddress

admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
