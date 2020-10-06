from django.shortcuts import render
from Market.models import Product, Category
# Create your views here.

def cart(request):
    navigation = Category.objects.all()
    return render(request, 'cart.html',
                  context={'navi': navigation})

def empty(request):
    navigation = Category.objects.all()
    return render(request, 'empty_section.html',
                  context={'navi': navigation})

def index(request):
    navigation = Category.objects.all()
    return render(request, 'index.html',
                  context={'navi': navigation})

def login(request):
    return render(request, 'login.html')

def phone(request):
    product = request.GET.get('product')
    test_subject = Product.objects.get(id= product)
    navigation = Category.objects.all()
    return render(request, 'phone.html',
                  context={'text': test_subject.name,
                           'pict': test_subject.picture_link,
                           'desc': test_subject.information,
                           'navi': navigation})

def smart(request):
    product = request.GET.get('category')
    test_subject = Product.objects.filter(category_id= product)
    navigation = Category.objects.all()
    category_name = Category.objects.get(id= product)
    return render(request, 'smartphones.html',
                  context = {'test': test_subject,
                             'category': category_name,
                             'navi': navigation})