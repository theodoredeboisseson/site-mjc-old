from django.urls import path
from .views import checkout, payment

urlpatterns = [
    path('checkout', checkout, name='checkout'),
    path('payment', payment, name='payment'),
]
