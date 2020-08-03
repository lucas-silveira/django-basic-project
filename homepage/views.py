from django.shortcuts import render, redirect
from django.contrib.auth import logout


def homepage(request):
    return render(request, 'homepage.html')


def custom_logout(request):
    logout(request)
    return redirect('homepage')
