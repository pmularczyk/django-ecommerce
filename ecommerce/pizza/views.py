from django.shortcuts import render

from .models import Customer, Item, OrderItem, Order

def home(request):
    return render(request, 'pizza/home.html', {})
