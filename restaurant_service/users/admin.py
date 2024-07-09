from django.contrib import admin
from .models import *

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating')
    list_filter = ('rating',)
    search_fields = ('name', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('fooditem','item_qty', 'user', 'created_at')

    def fooditem(self, obj):
        return obj.item.name

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID', 'orderedby', 'total_price', 'created_at')

    def orderID(self, obj):
        return f"order#{obj.id}"
    
    def orderedby(self, obj):
        return f"{obj.fname} {obj.lname}"

admin.site.register(OrderItem)

@admin.register(Profile) 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('userName', 'fullname') 

    def userName(self, obj):
        return f"{obj.user}"

    def fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"    
