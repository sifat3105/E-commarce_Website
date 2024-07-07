from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random
import string



User = get_user_model()
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    display_name = models.CharField(max_length=15, blank=True, null=True)
    
    def generate_otp(self):
        self.otp = ''.join(random.choices(string.digits, k=6))
        self.otp_created_at = timezone.now()
        self.save()

    def otp_is_valid(self):
        return self.otp_created_at + timedelta(minutes=10) > timezone.now()
    
    def __str__(self):
        return str(self.user.username)
    
    
    
    
class forget_otp(models.Model):
    otp = models.CharField(max_length=6, blank=True,null=True)
    email = models.CharField(max_length=30, blank= True, null= True)
    
    
    def otp_is_valid(self):
        return self.otp_created_at + timedelta(minutes=10) > timezone.now()
    
    