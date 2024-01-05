from django.urls import path
from . import  views

urlpatterns = [
    path('',views.loginCustomer,name='login')
]