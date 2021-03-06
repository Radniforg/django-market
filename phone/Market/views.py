from django.shortcuts import render, redirect
from Market.models import Product, Category, Article, Order, Cart, CustomUser
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone

User = get_user_model()


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')
    return render(request, 'login.html')


def logout_request(request):
    logout(request)
    return redirect('index')


def cart(request):
    navigation = Category.objects.all()
    if request.user.is_authenticated:
        email = request.user.email
        cart_check = CustomUser.objects.filter(email=email)[0].order_set.filter(status=0)
        if not cart_check:
            current_order = Order.objects.create(user_id=CustomUser.objects.filter(email=email)[0].id)
            current_order.save()
        else:
            current_order = cart_check[0]
        cart_inside = current_order.cart_set.all()
        total = 0
        for test_product in cart_inside:
            total += test_product.amount
        if request.method == 'POST':
            if request.POST['verification'] == "True":
                current_order.status = 1
                current_order.creation = timezone.now()
                current_order.total = total
                current_order.save()
                return redirect('index')
            else:
                merch_id = request.POST['merchandise_id']
                product = cart_inside.filter(product=merch_id)
                if product:
                    product[0].amount = product[0].amount + 1
                    total += 1
                    product[0].save()
                if not product:
                    addition = Cart.objects.create(product_id=merch_id,
                                                   order_id=current_order.id,
                                                   amount=1)
                    total += 1
                    addition.save()
            cart_inside = current_order.cart_set.all()
        return render(request, 'cart.html',
                      context={'navi': navigation,
                               'cart': cart_inside,
                               'total': total})
    else:
        return redirect('login')


def empty(request):
    navigation = Category.objects.all()
    return render(request, 'empty_section.html',
                  context={'navi': navigation})


def index(request):
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


def phone(request):
    product = request.GET.get('product')
    current_product = Product.objects.get(id=product)
    navigation = Category.objects.all()
    return render(request, 'phone.html',
                  context={'text': current_product.name,
                           'pict': current_product.picture_link,
                           'desc': current_product.information,
                           'navi': navigation,
                           'product_id': current_product.id})


def category(request):
    product = request.GET.get('category')
    test_subject = Product.objects.filter(category_id=product)
    navigation = Category.objects.all()
    category_name = Category.objects.get(id=product)
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(test_subject, 2)
    page = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if page.has_previous():
        prev_page = f'?category={product}&page={page.previous_page_number()}'
    if page.has_next():
        next_page = f'?category={product}&page={page.next_page_number()}'

    return render(request, 'category.html',
                  context={'test': page,
                           'category': category_name,
                           'navi': navigation,
                           'prev_page_url': prev_page,
                           'next_page_url': next_page,
                           'current_page': current_page
                           })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = None
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(password=raw_password)
            login(request)
            return redirect('index')
        else:
            print(form.errors)
            msg = form.errors
            return render(request, 'signup.html', {'form': form,
                                                   'msg': msg})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
