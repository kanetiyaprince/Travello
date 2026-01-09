from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

# from django.contrib import auth

# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        # user = auth.authenticate(username=username,password=password1)
        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request,user)    
            messages.info(request,'Welcome back ')
            return redirect('/')

        else:
            messages.info(request,'invalid credential')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,email=email,last_name=last_name)

                user.save()
                print('user created')
                return redirect('login')
            
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    
    else:
        return render(request,'register.html')
    
@never_cache
def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect('/')