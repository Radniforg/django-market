from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.



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
    status = models.BooleanField(default=False)
    creation = models.DateTimeField(default=timezone.now())
    products = models.ManyToManyField(Product, through='Cart')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product', 'order')