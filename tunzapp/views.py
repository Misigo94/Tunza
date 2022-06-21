
from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *

# Create your views here.
def home(request):
    '''view for home'''
    return render(request, 'tunzapp/home.html')



def signup(request):
    '''view for signup'''
    form = CreateUserForm()
    
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
            
    context ={
        'form': form,
        }        
    
    return render(request,'accounts/register.html', context)



def login_page(request):
    '''view for login'''
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(username,password,user)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.info(request, 'Check username or password !')
        
    return render(request, 'accounts/login.html')   
     


def logout_user(request):
    '''logout user'''
    logout(request)
    return redirect('login')