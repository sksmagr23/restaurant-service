from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating')
    list_filter = ('rating',)
    search_fields = ('name', 'description')