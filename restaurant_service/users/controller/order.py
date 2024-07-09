from django.shortcuts import redirect, render
from users.models import Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, "orders/index.html", context)

@login_required
def view(request, id):
    order = Order.objects.filter(id=id).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request, "orders/view.html", context)