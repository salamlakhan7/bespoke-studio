from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone_number")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_artisan = False  # Ensure they are saved as a Customer
        if commit:
            user.save()
        return user
    


class ArtisanSignupForm(UserCreationForm):
    # Custom field for artisans
    phone_number = forms.CharField(max_length=15, required=True, label="Business Phone Number")
    
    class Meta(UserCreationForm.Meta):
        model = User
        # Ensure 'email' and 'phone_number' are included in the signup
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number',)
        
# studio/forms.py
from django import forms
from .models import StockItem

class StockItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply professional styling to all fields
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white focus:border-amber-500 outline-none transition'
            })

    class Meta:
        model = StockItem
        fields = ['title', 'description', 'price', 'image', 'is_available']