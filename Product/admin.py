from django.contrib import admin
from .models import Category,SubCategory, Product, Banner, Deal, Banner_2
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Banner)
admin.site.register(Banner_2)
admin.site.register(Deal)