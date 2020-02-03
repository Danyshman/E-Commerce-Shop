from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User


def create(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        re_password = request.data['re_password']

        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with such Email is already exists!')
            else:
                user = User.objects.create_user(email, password)
                user.save()
                auth.login(request, user)
                messages.success(request, 'Account successfully created!')
                return redirect('profile')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect("index")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('index')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')







