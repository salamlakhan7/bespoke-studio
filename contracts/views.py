from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from studio.models import ChatRoom # Ensure this import is correct

@login_required
def owner_dashboard(request):
    # Security: Ensure only artisans can see this page
    if not request.user.is_artisan:
        from django.shortcuts import redirect
        return redirect('customer_dashboard')

    # Fetch all rooms where this user is the assigned artisan
    active_chats = ChatRoom.objects.filter(artisan=request.user).order_by('-created_at')

    return render(request, 'contracts/owner_dashboard.html', {
        'active_chats': active_chats,
    })