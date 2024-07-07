from django.urls import reverse
from Auth_App.models import profile
# from product.models import Category, Product

def account_context(request):
    # categories = Category.objects.all()
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
        # 'Profile': profile.objects.all(),
        # 'categories': categories
    }
    