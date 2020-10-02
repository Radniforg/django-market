from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'cart.html')

def empty(request):
    return render(request, 'empty_section.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def phone(request):
    return render(request, 'phone.html')

def smart(request):
    return render(request, 'smartphones.html')