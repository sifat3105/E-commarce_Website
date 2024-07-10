from django.db import models
from django.contrib.auth.models import User
from Product.models import Product
from django.utils import timezone
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    added_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        # Calculate the subtotal as a Decimal
        self.subtotal =(self.product.price)* self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s wishlist item: {self.product.name}"