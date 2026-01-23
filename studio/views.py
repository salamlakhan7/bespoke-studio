import io
import time
import uuid
import base64
import requests 
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image

# --- INTERNAL IMPORTS ---
from .models import DesignConcept, ChatRoom, Message, StockItem
from .forms import ArtisanSignupForm, CustomerSignUpForm, StockItemForm
from .decorators import customer_required, artisan_required

User = get_user_model()

# =================================================================
# 🛡️ AUTHENTICATION & ACCESS CONTROL
# =================================================================

def signup_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/signup_customer.html', {'form': form})

def signup_artisan(request):
    if request.method == 'POST':
        form = ArtisanSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_artisan = True
            user.save()
            login(request, user)
            return redirect('owner_dashboard')
    else:
        form = ArtisanSignupForm()
    return render(request, 'registration/signup_artisan.html', {'form': form})

@login_required
def role_based_redirect(request):
    if request.user.is_artisan:
        return redirect('owner_dashboard')
    return redirect('customer_dashboard')

# =================================================================
# 🎨 CUSTOMER STUDIO & AI ENGINE
# =================================================================

@customer_required
def customer_dashboard(request):
    generated_images = []
    user_prompt = ""
    
    if request.method == "POST":
        user_prompt = request.POST.get('prompt')
        for i in range(5):
            unique_seed = int(time.time() * 1000) + (i * 888)
            clean_prompt = user_prompt.replace(" ", "%20")
            img_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1024&height=1024&seed={unique_seed}&nologo=true&model=flux"
            generated_images.append(img_url)
            time.sleep(0.5) 

    return render(request, 'studio/customer_dashboard.html', {
        'generated_images': generated_images, 
        'user_prompt': user_prompt
    })

@customer_required
def save_to_vault(request):
    if request.method == "POST":
        img_url = request.POST.get('img_base64')
        prompt = request.POST.get('prompt')
        
        if img_url:
            try:
                if img_url.startswith('/media/'):
                    relative_path = img_url.replace('/media/', '')
                    if default_storage.exists(relative_path):
                        with default_storage.open(relative_path, 'rb') as f:
                            data = ContentFile(f.read())
                            concept = DesignConcept(user=request.user, prompt=prompt)
                            file_name = f"vault_{uuid.uuid4().hex[:8]}.jpg"
                            concept.image.save(file_name, data, save=True)
                        return JsonResponse({'status': 'success'})
                else:
                    response = requests.get(img_url, timeout=25)
                    if response.status_code == 200:
                        data = ContentFile(response.content)
                        concept = DesignConcept(user=request.user, prompt=prompt)
                        file_name = f"ai_vision_{uuid.uuid4().hex[:8]}.jpg"
                        concept.image.save(file_name, data, save=True)
                        return JsonResponse({'status': 'success'})

            except Exception as e:
                print(f"Vault Save Error: {e}")
                
    return JsonResponse({'status': 'error'}, status=400)

@customer_required
def saved_concepts(request):
    sort_by = request.GET.get('sort', 'newest')
    query = request.GET.get('q', '') 
    concepts = DesignConcept.objects.filter(user=request.user)
    if query:
        concepts = concepts.filter(prompt__icontains=query)
    concepts = concepts.order_by('created_at' if sort_by == 'oldest' else '-created_at')
    return render(request, 'studio/saved_concepts.html', {
        'concepts': concepts, 
        'current_sort': sort_by, 
        'query': query
    })

# =================================================================
# ⚒️ ARTISAN INVENTORY & SHOWROOM
# =================================================================

@artisan_required
def owner_dashboard(request):
    active_chats = ChatRoom.objects.filter(artisan=request.user).order_by('-created_at')
    return render(request, 'contracts/owner_dashboard.html', {'active_chats': active_chats})

@artisan_required
def manage_inventory(request):
    if request.method == 'POST':
        form = StockItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.artisan = request.user
            item.save()
            return redirect('manage_inventory')
    inventory = StockItem.objects.filter(artisan=request.user).order_by('-created_at')
    return render(request, 'contracts/manage_inventory.html', {
        'form': StockItemForm(), 
        'inventory': inventory
    })

def public_showroom(request):
    items = StockItem.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'studio/showroom.html', {'items': items})

@login_required
def item_detail(request, item_id):
    item = get_object_or_404(StockItem, id=item_id)
    return render(request, 'studio/item_detail.html', {
        'item': item,
        'company_stats': {
            'experience': '15+ Years',
            'rating': '4.9/5',
            'delivery': 'Fast & Secure',
            'material': 'Premium Grade'
        }
    })

# =================================================================
# 💬 REAL-TIME NEGOTIATION HUB
# =================================================================

@login_required
def negotiation_page(request):
    room_id = request.GET.get('room_id')
    item_id = request.GET.get('item_id')
    ref_image = request.GET.get('img')
    ref_prompt = request.GET.get('prompt')
    
    referenced_item = None
    if item_id:
        referenced_item = get_object_or_404(StockItem, id=item_id)

    artisan_user = User.objects.filter(is_artisan=True).first()

    if request.user.is_artisan:
        if not room_id: 
            return redirect('owner_dashboard')
        room = get_object_or_404(ChatRoom, id=room_id, artisan=request.user)
    else:
        room, created = ChatRoom.objects.get_or_create(
            customer=request.user, 
            artisan=artisan_user
        )

    return render(request, 'studio/negotiation.html', {
        'room_id': room.id,
        'chat_history': room.messages.all().order_by('timestamp'),
        'chat_partner': room.customer if request.user.is_artisan else room.artisan,
        'item_name': ref_prompt,
        'item_image': ref_image,
        'referenced_item': referenced_item,
    })

@login_required
def upload_chat_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        filename = default_storage.save(f"chat_uploads/{image_file.name}", image_file)
        file_url = default_storage.url(filename)
        return JsonResponse({'status': 'success', 'url': file_url})
    return JsonResponse({'status': 'error'}, status=400)