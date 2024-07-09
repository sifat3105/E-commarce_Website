from django.urls import reverse
from Auth_App.models import profile
from Product.models import Category, Product

def account_context(request):
    categories = Category.objects.all()
    first_name = None
    log_reg = 'Log In / Sign Up'
    log_reg_link = reverse('login_registration')
    
    if request.user.is_authenticated:
        first_name = request.user.first_name
        log_reg = request.user.username
        log_reg_link = reverse('account')
    
    return {
        'first_name': first_name,
        'log_reg': log_reg,
        'log_reg_link': log_reg_link,
        #'Profile': profile.objects.all(),
        'categories': categories
    }
    
def product_view(request):
    products = Product.objects.all()
    total_product = len(products)
    return{'products': products, 'total_product':total_product}

def check_user(request):
    if request.user.is_authenticated:
        user = request.user
        if user.is_superuser or user.is_staff:
            creation_dashboard = 'Creation Dashboard'
            creation_dashboard_link = reverse('creation_dashboard_view')
    return locals() 