from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]
            user.save()
            messages.success(request, "User Registered Successfully", 'success')
            return redirect('account:user_login')
    else:
        form = UserRegisterForm()
    return render(request, "account/register.html", {"form" : form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd["username"], password = cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "User Logged in Successfully", 'success')
                return redirect('note:home')
            else:
                messages.error(request, "Username or Password is wrong", 'danger')
                return redirect('account:user_login')
    else:
        form = UserLoginForm()
    return render(request, "account/login.html", {"form" : form})

def user_logout(request):
    logout(request)
    messages.success(request, "User Logged Out Successfully", 'success')
    return redirect("note:home")