from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# =================================================================
# 👤 USER IDENTITY & PROFILES
# =================================================================

class User(AbstractUser):
    """Extended user model for Bespoke Studio participants."""
    is_artisan = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({'Artisan' if self.is_artisan else 'Customer'})"

# =================================================================
# 💬 REAL-TIME CHAT & MESSAGING
# =================================================================

class ChatRoom(models.Model):
    """A secure channel for price negotiations between two parties."""
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='customer_chats'
    )
    artisan = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='artisan_chats'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'artisan')

    def __str__(self):
        return f"Room: {self.customer.username} & {self.artisan.username}"

class Message(models.Model):
    """Individual data fragments (text/images) within a ChatRoom."""
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='chat_uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} at {self.timestamp}"

# =================================================================
# 📦 INVENTORY & SHOWROOM MANAGEMENT
# =================================================================

class StockItem(models.Model):
    """Ready-to-ship handcrafted furniture listed in the showroom."""
    artisan = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='inventory'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='stock_items/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# =================================================================
# 🧠 AI DESIGN VAULT
# =================================================================

class DesignConcept(models.Model):
    """User-generated AI concepts saved from the design studio."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prompt = models.TextField()
    image = models.ImageField(upload_to='designs/') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.prompt[:20]}"