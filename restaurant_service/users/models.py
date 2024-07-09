from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(6)])

    def _str_(self):
        return self.name
  
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    item_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, null=False)
    lname = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    address = models.TextField(null=False)
    total_price = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.fname}- orderId:{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE) 
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def _str_(self):
        return self.order.id   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user.username

    