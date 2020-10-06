from django.shortcuts import render
from Market.models import Product, Category
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
    test_subject = Product.objects.first()
    return render(request, 'phone.html',
                  context={'text': test_subject.name,
                           'pict': test_subject.picture_link,
                           'desc': test_subject.information},)

def smart(request):
    return render(request, 'smartphones.html')