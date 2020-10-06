from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
# class User(AbstractUser):
#     pass


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    picture_link = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    information = models.TextField()
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name