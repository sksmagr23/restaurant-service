from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import MenuItem

def home(request):
    return render(request, 'users/home.html')

@login_required
def menu(request):
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    return render(request, 'users/menu.html', {'menu_items': menu_items})

@login_required
def cart_page(request):
    return render(request, 'users/cart.html')