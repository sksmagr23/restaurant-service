from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from users.models import MenuItem, Cart

def addtoCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            item_id = int(request.POST.get('item_id'))
            item_check = MenuItem.objects.get(id=item_id)
            if (item_check):
                if (Cart.objects.filter(user=request.user.id, item_id=item_id)):
                    return JsonResponse({'status': "Item is already in cart"}) 
                else:
                    item_qty = int(request.POST.get('item_qty')) 
                    Cart.objects.create(user=request.user, item_id=item_id, item_qty=item_qty)
                    return JsonResponse({'status': "Item added to cart successfully"}) 
                    
            else:
                return JsonResponse({'status': "No such item found in menu"})        

        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')  


def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, "users/cart.html", context)        

def updatecart(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        if (Cart.objects.filter(user=request.user, item_id=item_id)):
            item_qty = int(request.POST.get('item_qty'))
            cart = Cart.objects.get(item_id=item_id, user=request.user)
            cart.item_qty = item_qty
            cart.save()
            return JsonResponse({'status':"updated successfully"})
    return redirect('/')
  
def deletecartitem(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        if (Cart.objects.filter(user=request.user, item_id=item_id)):
            cartitem = Cart.objects.get(item_id=item_id, user=request.user)
            cartitem.delete()
            return JsonResponse({'status':"Deleted item successfully"})
    return redirect('/')

