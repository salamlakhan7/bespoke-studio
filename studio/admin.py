from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# This tells Django to use the standard UserAdmin but for our custom User model
admin.site.register(User, UserAdmin)
