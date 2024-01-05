from django.contrib import admin
from django.contrib.auth.models import User
from .models import  CustomerUser,UserAddress

# Register your models here.
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['is_active','name']
    search_fields = ['name']
    list_filter = ['is_active']
    ordering = ['name']
    list_editable = ['name']
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['customerUser','address']
    search_fields = ['address']
admin.site.register(CustomerUser,CustomerUserAdmin)
admin.site.register(UserAddress,UserAddressAdmin)
