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



# import requests
# from django.utils.deprecation import MiddlewareMixin
# from user_agents import parse

# class UserInformationMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         # Get the user's IP address
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')

#         # Get the user's device information
#         user_agent = request.META.get('HTTP_USER_AGENT', '')
#         user_agent_info = parse(user_agent)

#         # Example of using ipstack for geolocation (replace 'your_api_key' with your actual API key)
#         location = None
#         if ip:
#             response = requests.get(f'https://api.exchangeratesapi.io/history?base=GBP&symbols=USD,GBP,EUR,CAD,SEK')
#             if response.status_code == 200:
#                 location = response.json()

#         # Add the information to the request
#         request.user_ip = ip
#         request.user_device = user_agent_info
#         request.user_location = location
