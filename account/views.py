from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User
from django.http import HttpResponse


def create(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with such Email is already exists!')
                return HttpResponse()
            else:
                user = User.objects.create_user(email, password)
                user.save()
                auth.login(request, user)
                messages.success(request, 'Account successfully created!')
                return redirect("account:user_profile")
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
            return redirect('account:user_profile')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('index')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def user_profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'account/account-profile.html')
        else:
            return redirect('index')
    if request.method == 'POST':
        data = dict(request.POST)
        user = request.user
        if data['new_password'] != '' and data['new_password'] == data['confirm_password']:
            user.set_password(data['new_password'])
        if data['username'] != '':
            if User.objects.filter(username=data['username']).exists():
                # SHOW ALERT SHUCH USERNAME ALREADY EXISTS
                return redirect('index')
            else:
                user.__setattr__('username', data['username'])
        for key, value in data.items():
            if key != 'csrfmiddlewaretoken':
                print(key, value)
                user.__setattr__(key, value[0])
        user.save()
        return redirect('account:user_profile')








