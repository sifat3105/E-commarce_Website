# Generated by Django 5.0.6 on 2024-07-07 19:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_small', models.CharField(help_text='Small title above main title', max_length=255)),
                ('title_large', models.TextField(help_text='Main large title')),
                ('image', models.ImageField(help_text='Image for the banner', upload_to='banners/')),
                ('button_text', models.CharField(help_text='Text displayed on the button', max_length=100)),
                ('button_link', models.URLField(help_text='URL that the button links to')),
            ],
        ),
        migrations.CreateModel(
            name='Banner_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_title', models.CharField(help_text='Small title above the main title', max_length=255)),
                ('large_title', models.TextField(help_text='Main large title')),
                ('image', models.ImageField(help_text='Image for the banner', upload_to='banners/')),
                ('button_link', models.URLField(help_text='URL that the button links to')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cat_logo', models.ImageField(blank=True, null=True, upload_to='category_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the deal', max_length=255)),
                ('subtitle', models.CharField(blank=True, help_text='Subtitle of the deal', max_length=255, null=True)),
                ('description', models.TextField(blank=True, help_text='Description of the deal', null=True)),
                ('image', models.ImageField(help_text='Background image for the deal', upload_to='deals/')),
                ('new_price', models.DecimalField(decimal_places=2, help_text='New price of the deal', max_digits=10)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, help_text='Old price of the deal', max_digits=10, null=True)),
                ('countdown_end', models.DateTimeField(help_text='End date and time for the countdown')),
                ('product_link', models.URLField(help_text='Link to the product')),
                ('shop_link', models.URLField(help_text='Link to the shop page')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the brand', max_length=255)),
                ('image', models.ImageField(help_text='Logo of the brand', upload_to='brands/')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='Product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('warranty', models.CharField(blank=True, max_length=50, null=True)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Product.category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Product.subcategory')),
            ],
        ),
    ]
