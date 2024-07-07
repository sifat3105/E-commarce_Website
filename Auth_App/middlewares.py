# from django.shortcuts import redirect



# def not_verified_user(view_function):
#     def wrapped_view(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect('login_registration')
#         return view_function(request, *args, **kwargs)
#     return wrapped_view
        
        
# def verified_user(view_function):
#     def wrapped_view(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             # if request.user.username == 'admin':
#             #     return redirect('logout')
#             return redirect('home')
#         return view_function(request, *args, **kwargs)
#     return wrapped_view