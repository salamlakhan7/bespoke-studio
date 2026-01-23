from django.shortcuts import render
from django.http import HttpResponse ,HttpResponse
from b_shop.studio.decorators import customer_required, artisan_required
from django.contrib.auth.decorators import login_required

@artisan_required
def owner_dashboard(request):
    return render(request, 'contracts/owner_dashboard.html')