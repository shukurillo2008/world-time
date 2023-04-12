from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'dasturga kirdingiz')
            return redirect('main_page')
        else:
            messages.error(request, 'parol yoki login hato')
    return render(request, 'account/login.html')
    # else:
    #     username = request.GET.get(register_user.username)
    #     password = request.GET.get(register_user.password)
    #     login(request, user)
    #     return redirect('main_page')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        User.objects.create_user(
            username=username,
            password=password
        )
        user = authenticate(username=username , password=password)
        login(request, user)

        return redirect('main_page')
    return render(request, 'account/register.html')


def log_out(request):
    logout(request)
    return redirect('main_page')