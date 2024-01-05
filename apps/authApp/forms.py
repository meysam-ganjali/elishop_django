from django import forms
from .models import  CustomerUser
class LoginForm(forms.Form):
    phone_number=forms.CharField(label="شماره تلفن", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'پسوورد خود را وارد کنید'}))
    password=forms.CharField(label="کلمه عبور",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'آدرس ایمیل خود را وارد کنید'}))