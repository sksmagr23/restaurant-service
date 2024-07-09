from django.contrib import admin
from .models import *

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating')
    list_filter = ('rating',)
    search_fields = ('name', 'description')

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)  
admin.site.register(Profile)  
