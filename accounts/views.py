from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.hashers import make_password
from . models import CustomUser
# Create your views here.

User=get_user_model()
def register_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        role=request.POST.get('role')
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'error': 'Email already exists'})
        # Create and save user with hashed password
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # secure hashing
            role=role
        )
        return redirect('all_user')# update leter with redirect to login
    return render(request,'accounts/register.html')

def all_user(request):
    users=CustomUser.objects.all()
    return render(request,"accounts/all_user.html",{'users':users})
    
def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
    return render (request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')