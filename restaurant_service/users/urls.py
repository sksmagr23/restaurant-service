from django.urls import path
from . import views
from users.controller import cart, checkout, order

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cart', cart.viewcart, name='cart'),
    path('add-to-cart', cart.addtoCart, name="addtocart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    path('my-orders', order.index, name="myorders"),
    path('view-order/<str:id>', order.view, name="orderview")
]