from django.urls import path
from .views import customer_dashboard

urlpatterns = [
    # ... other paths
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
]