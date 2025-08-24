from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = authenticate(request, username=uname, password=pwd)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
           
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        uemail = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if pwd1 != pwd2:
            messages.error(request,'Password does not match.')
            return render(request, 'register.html')
        
        if User.objects.filter(username = uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')
        
        if User.objects.filter(email = uemail).exists():
            messages.error(request, 'Email alread exists.')
            return render(request, 'register.html')
        
        user = User.objects.create_user(
            first_name = fname, 
            last_name = lname,
            username = uname,
            email = uemail,
            password=pwd1,
        )
        messages.success(request, "Registration successful! You are now logged in.")
        login(request,user)
        return redirect('dashboard')
    else:
        return render(request, 'register.html')

@login_required(login_url='login')
def upate_profile_view(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        uemail = request.POST['email']

        if User.objects.filter(username=uname).exclude(id=request.user.id).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'accounts/update_profile.html')

        if User.objects.filter(email=uemail).exclude(id=request.user.id).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'accounts/update_profile.html')

        request.user.username = uname
        request.user.email = uemail
        request.user.first_name = fname
        request.user.last_name = lname
        request.user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('dashboard')
     
    return render(request, 'update_profile.html')