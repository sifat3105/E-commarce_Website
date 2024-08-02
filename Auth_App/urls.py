from django.urls import path
from .views import login_register_view, verify, details_update, email_verifiation, new_password, password_change_done, reset_password, logout_view, ssl_commarce, order_success, oder_fail

urlpatterns = [
    path('login_registration/', login_register_view, name='login_registration'),
    path('verify/<int:otp>/', verify, name='verify'),
    path('details_update/<int:id>/', details_update, name='details_update'),
    path('login_registration/forget/', email_verifiation, name= 'email_verifiation'),
    path('login_registration/forget/new_password/',new_password, name='new_password'),
    path('login_registration/forget/new_password/password_change_done/',password_change_done, name='password_change_done'),
    path('reset_password/',reset_password, name='reset_password'),
    path('logout/',logout_view, name='logout'),
    path('ssl_commarce/', ssl_commarce, name='ssl_commarce'),
    path('success/', order_success, name='order_success'),
    path('fail/', oder_fail, name='oder_fail'),
]