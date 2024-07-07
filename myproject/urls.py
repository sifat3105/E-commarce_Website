
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('auth/', include('Auth_App.urls')),
    path('account/', include('Account_Dashboard.urls')),
    path('product/', include('Product.urls')),

]
