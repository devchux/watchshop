from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    items = Item.objects.all().order_by('-date_added')[:3]
    context = {
        'title': 'Home',
        'items': items,
    }
    return render(request, 'ecom/home.html', context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'ecom/about.html', context)

def shop(request):
    items = Item.objects.all().order_by('-date_added')
    context = {
        'title': 'Our Shop',
        'items': items,
    }
    return render(request, 'ecom/shop.html', context)

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'title': 'Product Details',
        'item': item
    }
    return render(request, 'ecom/details.html', context)