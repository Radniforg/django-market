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
    smol_test = Category.objects.all()
    return render(request, 'phone.html',
                  context={'text': test_subject.name,
                           'pict': test_subject.picture_link,
                           'desc': test_subject.information,
                           'pretext': smol_test},)

def smart(request):
    test_category_id = 1
    test_subject = Product.objects.filter(category_id= test_category_id)
    category_name = Category.objects.get(id= test_category_id)
    return render(request, 'smartphones.html',
                  context = {'test': test_subject,
                             'category': category_name})