from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Shop(models.Model):
    name = models.CharField(max_length=40)
    state = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=40)

class Product(models.Model):
    name = models.CharField(max_length=40)