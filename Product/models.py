import uuid
from django.db import models
from .utils import convert_image_size


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cat_logo = models.ImageField(upload_to='category_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount =models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    warranty = models.CharField(max_length=50, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/', blank=True, null=True)
    image6 = models.ImageField(upload_to='products/', blank=True, null=True)
    image7 = models.ImageField(upload_to='products/', blank=True, null=True)
    rating = models.PositiveIntegerField( null=True, blank=True)
    num_reviews = models.PositiveIntegerField(default=0)
    show_rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.old_price != 0:
            discount = self.old_price - self.price
            self.discount = round((discount / self.old_price) * 100)
        else:
            self.discount = 0
            
        try:
            self.image = convert_image_size(self.image, 10, 9)
            self.image2 = convert_image_size(self.image2, 10, 9)
            self.image3 = convert_image_size(self.image3, 10, 9)
            self.image4 = convert_image_size(self.image4, 10, 9)
            self.image5 = convert_image_size(self.image5, 10, 9)
            self.image6 = convert_image_size(self.image6, 10, 9)
            self.image7 = convert_image_size(self.image7, 10, 9)
        except:
            None
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    
class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField( null=True, blank=True)
    reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}'s Reviews: {self.comment}"
    
class Banner(models.Model):
    title_small = models.CharField(max_length=255, help_text="Small title above main title")
    title_large = models.TextField(help_text="Main large title")
    image = models.ImageField(upload_to='banners/', help_text="Image for the banner")
    button_text = models.CharField(max_length=100, help_text="Text displayed on the button")
    button_link = models.URLField(max_length=200, help_text="URL that the button links to")
    
    def save(self, *args, **kwargs):
        img = convert_image_size(self.image, 13, 3)
        self.image = img
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title_large


class Banner_2(models.Model):
    small_title = models.CharField(max_length=255, help_text="Small title above the main title")
    large_title = models.TextField(help_text="Main large title")
    image = models.ImageField(upload_to='banners/', help_text="Image for the banner")
    button_link = models.URLField(max_length=200, help_text="URL that the button links to")
    
    def __str__(self):
        return self.large_title


class Deal(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the deal")
    subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Subtitle of the deal")
    description = models.TextField(blank=True, null=True, help_text="Description of the deal")
    image = models.ImageField(upload_to='deals/', help_text="Background image for the deal")
    new_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="New price of the deal")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Old price of the deal")
    countdown_end = models.DateTimeField(help_text="End date and time for the countdown")
    product_link = models.URLField(max_length=200, help_text="Link to the product")
    shop_link = models.URLField(max_length=200, help_text="Link to the shop page")

    def __str__(self):
        return self.title
    
class FeaturedBrand(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the brand")
    image = models.ImageField(upload_to='brands/', help_text="Logo of the brand")

    def __str__(self):
        return self.name


