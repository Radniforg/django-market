from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Это не email!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser должен относиться '
                             'к сотрудникам (is_staff error)')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser должен быть '
                             'суперюзером (is_superuser error)')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'),
                              unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    picture_link = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    information = models.TextField()
    timezone = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=128)
    information = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    products = models.ManyToManyField(Product)

class Order(models.Model):
    order = models.BooleanField(default= False)
    products = models.ManyToManyField(Product, through='Cart')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        unique_together = ('theme', 'article')