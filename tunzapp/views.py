from django.shortcuts import render

# Create your views here.
def home(request):
    '''view for home'''
    return render(request, 'tunza/home.html')

def signup(request):
    '''view for signup'''
    return render(request,'tunza/signup.html')

def login(request):
    '''view for login'''
    
    return render(request, 'tunza/login.html') 

