from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from .models import User
from django.http import HttpResponse, HttpResponseRedirect


def create(request):
    if request.method == 'POST':
        data = dict(request.POST)
        if data['password'][0] == data['re_password'][0]:
            if User.objects.filter(email=data['email'][0]).exists():
                messages.error(request, 'User with such Email is already exists!')
                return HttpResponse()
            if data['username'][0] != '':
                if User.objects.filter(username=data['username'][0]).exists():
                    # SHOW ALERT SUCH USERNAME ALREADY EXISTS
                    return redirect('index')
            user = User.objects.create_user(data['email'][0], data['password'][0])
            for key, value in data.items():
                if key != 'csrfmiddlewaretoken' and key != 'new_password' and key != 'username':
                    user.__setattr__(key, value[0])
            user.save()
            auth.login(request, user)
            messages.success(request, 'Account successfully created, please login!')
            return redirect('user:user_profile', user_id=user.id)
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('user:login')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return HttpResponseRedirect('/user/{}/profile/'.format(user.id))
        else:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect('/user/login/')
    if request.method == 'GET':
        return render(request, 'account/account-signin.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def user_profile(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'account/account-profile.html')

        elif request.method == 'POST':
            data = dict(request.POST)
            user = request.user
            if data['new_password'] == data['confirm_password']:
                if data['new_password'] != '':
                    data.pop('new_password')
                    data.pop('confirm_password')
                else:
                    user.set_password(data['new_password'])
            if data['username'] != '':
                if User.objects.filter(username=data['username']).exists():
                    # SHOW ALERT SUCH USERNAME ALREADY EXISTS
                    return redirect('index')
                else:
                    user.__setattr__('username', data['username'][0])
                    data.pop('username')
            if request.FILES:
                user.avatar = request.FILES['avatar']
            for key, value in data.items():
                if key != 'csrfmiddlewaretoken' and key != 'new_password' and key != 'username':
                    print(request.POST)
                    user.__setattr__(key, value[0])
            user.save()
            return render(request, 'account/account-profile.html')


def wishlist(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'account/account-wishlist.html')








