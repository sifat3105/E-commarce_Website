from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
User = get_user_model()
class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, null=True, blank=True,default="street_address")
    city = models.CharField(max_length=100, null=True, blank=True, default="city")
    state = models.CharField(max_length=100, null=True, blank=True, default="state")
    postal_code = models.CharField(max_length=20, null=True, blank=True, default="postal_code")
    country = models.CharField(max_length=100, null=True, blank=True, default="country")
    number = models.CharField(max_length=25, null=True, blank=True, default="number")

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"
    
class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, null=True, blank=True,default="street_address")
    city = models.CharField(max_length=100, null=True, blank=True, default="city")
    state = models.CharField(max_length=100, null=True, blank=True, default="state")
    postal_code = models.CharField(max_length=20, null=True, blank=True, default="postal_code")
    country = models.CharField(max_length=100, null=True, blank=True, default="country")
    number = models.CharField(max_length=25, null=True, blank=True, default="number")


    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"
