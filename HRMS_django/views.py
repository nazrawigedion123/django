
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = 'registration/login.html'



def home_view(request):
    return render(request,'myapp/home.html')


def about(request):
    return render(request, 'myapp/about.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'myapp/contact.html')


def services(request):
    return render(request, 'myapp/services.html')




