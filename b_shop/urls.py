from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# --- VIEW IMPORTS FROM STUDIO APP ---
from studio.views import (
    customer_dashboard,
    item_detail,
    owner_dashboard,
    negotiation_page,
    signup_artisan, 
    signup_customer, 
    role_based_redirect,
    upload_chat_image,
    manage_inventory,
    public_showroom,
    save_to_vault,      
    saved_concepts      #
)

# --- VIEW IMPORTS FROM MAIN APP ---
from .views import (
    landing_page, about_page, materials_page, contact_page, signup_choice
)

urlpatterns = [
    # 🌐 PUBLIC PAGES & LANDING
    path('', landing_page, name='landing'),
    path('about/', about_page, name='about'),
    path('materials/', materials_page, name='materials'),
    path('contact/', contact_page, name='contact'),
    
    # 🔐 AUTHENTICATION & ACCESS
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_choice, name='signup_choice'),
    path('signup/customer/', signup_customer, name='signup_customer'),
    path('signup/artisan/', signup_artisan, name='signup_artisan'),
    path('dashboard/redirect/', role_based_redirect, name='role_redirect'),
    
    # 💎 CUSTOMER AI STUDIO & DESIGN VAULT
    path('studio/dashboard/', customer_dashboard, name='customer_dashboard'),
    path('studio/save-concept/', save_to_vault, name='save_to_vault'),
    path('studio/vault/', saved_concepts, name='saved_concepts'),
    
    # 🏗️ ARTISAN MANAGEMENT & SHOWROOM
    path('contracts/panel/', owner_dashboard, name='owner_dashboard'),
    path('studio/inventory/', manage_inventory, name='manage_inventory'),
    path('studio/showroom/', public_showroom, name='public_showroom'),

    # 💬 CHAT, NEGOTIATION & DETAIL VIEW
    # path('studio/negotiate/', negotiation_page, name='start_negotiation'),
    path('negotiate/', negotiation_page, name='negotiation_page'),
    path('studio/upload-chat-image/', upload_chat_image, name='upload_chat_image'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    
    # ⚙️ SYSTEM ADMIN
    path('admin/', admin.site.urls),
]

# 🖼️ STATIC & MEDIA FILE HANDLING
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)