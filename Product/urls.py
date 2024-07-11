from django.urls import path
from .views import *
urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('', product_view, name='product_view'),
    path('<uuid:uuid>/', right_product_view, name='right_product_view'),
    path('create/banner/', banner_create_view, name='create_banner'),
    path('create/banner2/', banner2_create_view, name='create_banner2'),
    path('create/deal/', deal_create_view, name='create_deal'),
    path('create/featured_brand/', featured_brand_create_view, name='create_featured_brand'),
    path('success/', success_view, name='success'),
    path('creation/dashboard/view/', creation_dashboard_view, name='creation_dashboard_view'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)