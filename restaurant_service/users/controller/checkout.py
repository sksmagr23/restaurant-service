from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from users.models import Cart, Order, OrderItem, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.item.price * item.item_qty

    userprofile = Profile.objects.filter(user=request.user).first()    

    context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile}
    return render(request, "users/checkout.html", context)

@login_required
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user  
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')   
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.item.price * item.item_qty

        neworder.total_price = cart_total_price   
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                item=item.item,
                price=item.item.price,
                quantity=item.item_qty
            )

        Cart.objects.filter(user=request.user).delete()

        messages.success(request, "Your order has been placed successfully")     

    return redirect('/menu')    
