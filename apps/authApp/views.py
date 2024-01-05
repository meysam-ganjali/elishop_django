from django.shortcuts import render

from apps.authApp.forms import LoginForm
from .models import  CustomerUser
from django.contrib.auth import login,logout
from django.http import HttpResponse

def loginCustomer(request):
    context={
        'login_form': LoginForm()
    }
    if request.method == 'POST':
        # form = LoginForm(request.POST)

        username = request.POST['phone_number']
        password = request.POST['password']

        try:
            user = CustomerUser.objects.get(phone_number=username)
        except CustomerUser.DoesNotExist:
            return render(request, 'authApp/login.html', context=context)
        if username == user.phone_number and password == user.password:

            return HttpResponse('درستتتتتت')
    else:
        return render(request,'authApp/login.html',context)
