from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from studio.forms import CustomerSignUpForm

def landing_page(request): return render(request, 'landing.html')
def about_page(request): return render(request, 'about.html')
def materials_page(request): return render(request, 'materials.html')
def contact_page(request): return render(request, 'contact.html')

def signup_choice(request):
    return render(request, 'registration/choose_role.html')

def signup_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def login_redirect(request):
    if request.user.is_artisan:
        return redirect('owner_dashboard')
    return redirect('customer_dashboard')

# THE REDIRECT LOGIC (Crucial for your ImportError)
@login_required
def role_based_redirect(request):
    if request.user.is_artisan:
        return redirect('owner_dashboard')
    return redirect('customer_dashboard')

# Traffic Controller for Login (Same as above, but keeping naming consistent)
def login_redirect(request):
    return role_based_redirect(request)