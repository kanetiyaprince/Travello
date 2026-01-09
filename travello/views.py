from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

@never_cache
@login_required(login_url='login')
def index(request):
    
    dests = Destination.objects.all()

    return render(request,'index.html',{'dests':dests})

@never_cache
@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@never_cache
@login_required(login_url='login')
def contact(request):
    return render(request,'contact.html')

@never_cache
@login_required(login_url='login')
def destination(request):
    return render(request,'destinations.html')

@never_cache
@login_required(login_url='login')
def news(request):
    return render(request,'news.html')