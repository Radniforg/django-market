from django.shortcuts import render
from Market.models import Product, Category, Article
from django.core.paginator import Paginator
# Create your views here.

def cart(request):
    #нужно сделать
    navigation = Category.objects.all()
    return render(request, 'cart.html',
                  context={'navi': navigation})

def empty(request):
    navigation = Category.objects.all()
    return render(request, 'empty_section.html',
                  context={'navi': navigation})

def index(request):
    #нужно придумать и настроить выдачу последних n позиций
    navigation = Category.objects.all()
    article = Article.objects.all().order_by('-date')
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(article, 2)
    page = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if page.has_previous():
        prev_page = f'?page={page.previous_page_number()}'
    if page.has_next():
        next_page = f'?page={page.next_page_number()}'
    return render(request, 'index.html',
                  context={'navi': navigation,
                           'articles': page,
                           'prev_page_url': prev_page,
                           'next_page_url': next_page,
                           'current_page': current_page
                           })

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
    #сюда надо влепить пагинатор, также сменить название шаблона
    product = request.GET.get('category')
    test_subject = Product.objects.filter(category_id= product)
    navigation = Category.objects.all()
    category_name = Category.objects.get(id=product)
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(test_subject, 1)
    page = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if page.has_previous():
        prev_page = f'?category={product}&page={page.previous_page_number()}'
    if page.has_next():
        next_page = f'?category={product}&page={page.next_page_number()}'

    return render(request, 'smartphones.html',
                  context = {'test': page,
                             'category': category_name,
                             'navi': navigation,
                             'prev_page_url': prev_page,
                             'next_page_url': next_page,
                             'current_page': current_page
                             })