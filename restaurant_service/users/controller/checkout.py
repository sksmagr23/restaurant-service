from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from users.models import Cart
from django.contrib.auth.decorators import login_required

def index(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.item.price * item.item_qty

    context = {'cartitems':cartitems, 'total_price':total_price}
    return render(request, "users/checkout.html", context)