from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def customer_required(view_func):
    """Only allows users who are NOT artisans (is_artisan=False)"""
    decorated_view_func = user_passes_test(
        lambda u: u.is_authenticated and not u.is_artisan,
        login_url='login' # Redirect to login if not authenticated
    )(view_func)
    return decorated_view_func

# def artisan_required(view_func):
#     """Only allows users who ARE artisans (is_artisan=True)"""
#     decorated_view_func = user_passes_test(
#         lambda u: u.is_authenticated and u.is_artisan,
#         login_url='login'
#     )(view_func)
#     return decorated_view_func

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def artisan_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_artisan:
            return view_func(request, *args, **kwargs)
        return redirect('customer_dashboard') # Send customers away from artisan tools
    return wrapper