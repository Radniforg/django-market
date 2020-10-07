"""phone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Market import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', views.cart, name='cart'),
    path('empty_section/', views.empty, name='empty_section'),
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('phone/', views.phone, name='phone'),
    path('sign/', views.signup, name='sign_up'),
    path('smartphones/', views.smart, name='smartphones'),
    path('error/', views.smart, name='error'),
    path('test/', views.login_request, name='test'),
    path('tset/', views.logout_request, name='tset')
]
