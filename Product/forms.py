from django import forms
from .models import Banner, Banner_2, Deal, FeaturedBrand, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'

class Banner2Form(forms.ModelForm):
    class Meta:
        model = Banner_2
        fields = '__all__'

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'

class FeaturedBrandForm(forms.ModelForm):
    class Meta:
        model = FeaturedBrand
        fields = '__all__'