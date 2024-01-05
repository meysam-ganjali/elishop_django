from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def index(request):
    context={
        'media_url':settings.MEDIA_URL
    }
    return render(request,'mainApp/index.html',context)
